import functools
import google.appengine.api.users
import flask


def login_required(func):
    @functools.wraps(func)
    def decorated_view(*args, **kwargs):
        if not google.appengine.api.users.get_current_user():
            return flask.redirect(google.appengine.api.users.create_login_url(flask.request.url))
        return func(*args, **kwargs)
    return decorated_view


def admin_required(func):
    @functools.wraps(func)
    def decorated_view(*args, **kwargs):
        if google.appengine.api.users.get_current_user():
            if not google.appengine.api.users.is_current_user_admin():
                flask.abort(401)  # Unauthorized
            return func(*args, **kwargs)
        return flask.redirect(google.appengine.api.users.create_login_url(flask.request.url))
    return decorated_view

import functools
import flask
import application.core.utils
import application.user.services


def login_required(func):
    @functools.wraps(func)
    def wrapper():
        sid = flask.request.cookies.get('sid')
        session = application.core.utils.Session(sid)

        if not session.valid:
            return flask.redirect('/login')

        user = application.user.services.fetch_by_email(session.email)
        if not user:
            return flask.redirect('/login')
        if not user.verified:
            return flask.redirect('/verify')
        return func()
    return wrapper

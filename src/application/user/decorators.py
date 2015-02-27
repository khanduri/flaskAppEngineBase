import functools
import flask
import application.core.session
import application.user.services


def login_required(func):
    @functools.wraps(func)
    def wrapper():
        sid = flask.request.cookies.get('sid')
        session = application.core.session.Session(sid)

        if not session:
            return flask.redirect('/')

        user = application.user.services.fetch_by_email(session.email)
        if not user:
            return flask.redirect('/')
        return func()
    return wrapper


def verified_login_required(func):
    @functools.wraps(func)
    def wrapper():
        sid = flask.request.cookies.get('sid')
        session = application.core.session.Session(sid)

        if not session:
            return flask.redirect('/')

        user = application.user.services.fetch_by_email(session.email)
        if not user and not user.verified:
            return flask.redirect('/')
        return func()
    return wrapper

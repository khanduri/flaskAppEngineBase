import datetime
import hashlib
import flask
import application.user.decorators
import application
import application.user.services
import application.core.utils
import application.user.forms


@application.user.decorators.login_required
def logout():
    sid = flask.request.cookies.get('sid')
    session = application.core.utils.Session(sid)
    session.remove()

    response = flask.make_response(flask.redirect('/login'))
    response.set_cookie('Set-Cookie', 'sid=None; expires=%s' % (datetime.datetime.now()))
    return response


def register():
    form = application.user.forms.UserForm(csrf_enabled=False)
    if form.validate_on_submit():

        email = form.data.get('email')
        if application.user.services.fetch_by_email(email) is not None:
            flash_messages = [('danger', 'Email already registered!')]
            return flask.render_template('index.html', flash_messages=flash_messages)

        first = form.data.get('first')
        last = form.data.get('last')
        password = form.data.get('password')
        passhash = hashlib.md5(password).hexdigest()

        session = application.core.utils.Session(None)
        ip = flask.request.remote_addr
        sid = session.set(email, ip)
        resp = flask.make_response(flask.redirect('/verify'))
        resp.set_cookie('sid', sid)

        application.user.services.create_new_user(first, last, email, passhash)
        return resp

    flash_messages = [('danger', 'Registration failed!')]
    return flask.render_template('index.html', flash_messages=flash_messages)


def verify():
    sid = flask.request.cookies.get('sid')
    session = application.core.utils.Session(sid)
    user = application.user.services.fetch_by_email(session.email)

    if not user:
        flash_messages = [('danger', 'Invalid info while running verification')]
        return flask.render_template('index.html', flash_messages=flash_messages)

    if user.verified:
        return flask.redirect('/login')

    verification_code = flask.request.args.get('verification_code')
    if verification_code != user.verification_code:
        return flask.render_template('verify.html')

    application.user.services.modify_user_validity(user.id, True)
    return flask.redirect('/login')


def login():
    sid = flask.request.cookies.get('sid')
    session = application.core.utils.Session(sid)
    user = application.user.services.fetch_by_email(session.email)

    if not user:
        form = application.user.forms.UserLoginForm(csrf_enabled=False)
        if form.validate_on_submit():
            email = form.data.get('email')
            password = form.data.get('password')
            passhash = hashlib.md5(password).hexdigest()
            user = application.user.services.fetch_by_login(email, passhash)
            if not user:
                flash_messages = [('danger', 'Unable to Login')]
                return flask.render_template('index.html', flash_messages=flash_messages)
        else:
            flash_messages = [('warning', ' Login form contains invalid data')]
            return flask.render_template('index.html', flash_messages=flash_messages)

    if not user.verified:
        return flask.render_template('verify.html')

    flash_messages = [('success', 'Welcome %s!' % user.first.capitalize())]
    return flask.render_template('index.html', flash_messages=flash_messages, user=user)

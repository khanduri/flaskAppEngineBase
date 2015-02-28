import hashlib
import flask
import application
import application.core.session
import application.user.decorators
import application.user.services
import application.user.forms
import application.user.mails


@application.user.decorators.login_required
def logout():
    return _clear_session_and_get_response(flask.redirect('/'))


def _clear_session_and_get_response(details):
    sid = flask.request.cookies.get('sid')
    session = application.core.session.Session(sid)
    session.remove()
    response = flask.make_response(details)
    response.set_cookie('sid', '')
    return response


def register():
    form = application.user.forms.UserForm(csrf_enabled=False)
    if form.validate_on_submit():

        email = form.data.get('email')
        if application.user.services.fetch_by_email(email) is not None:
            flash_messages = [('danger', 'Email already registered!')]
            return flask.render_template('login.html', flash_messages=flash_messages)

        first = form.data.get('first')
        last = form.data.get('last')
        password = form.data.get('password')
        passhash = hashlib.md5(password).hexdigest()

        user = application.user.services.create_new_user(first, last, email, passhash)
        return _set_session_and_get_response('index.html', user)

    flash_messages = [('danger', 'Registration failed!')]
    return flask.render_template('login.html', flash_messages=flash_messages)


def forgot():
    form = application.user.forms.UserEmailResetForm(csrf_enabled=False)

    if not form.is_submitted():
        return flask.render_template('forgot.html')

    if form.validate_on_submit():
        email = form.data.get('email')
        user = application.user.services.fetch_by_email(email)
        if user:
            application.user.mails.send_reset(email, user.first, user.reset_code)

        # NOTE: We still let the viewer see the flash message even if the user email doesn't exists!
        # We don't want to reveal info back of data that we're missing
        flash_messages = [('info', 'Verification email sent! Please check your email.')]
        return flask.render_template('forgot.html', flash_messages=flash_messages)
    return flask.render_template('forgot.html')


def reset():
    form = application.user.forms.UserPasswordResetForm(csrf_enabled=False)

    if not form.is_submitted():
        reset_code = flask.request.args.get('reset_code')
        email = flask.request.args.get('email')
        return flask.render_template('reset.html', reset_code=reset_code, email=email)

    if form.validate_on_submit():
        email = form.data.get('email')
        user = application.user.services.fetch_by_email(email)
        if user:
            reset_code = form.data.get('reset_code')
            if reset_code == user.reset_code:
                password = form.data.get('password')
                passhash = hashlib.md5(password).hexdigest()
                application.user.services.modify_user(user.id, passhash=passhash)

                return _set_session_and_get_response('index.html', user, not_verified=not user.verified)
    return flask.redirect('/')


@application.user.decorators.login_required
def verify():
    session = application.core.session.get_session()
    if not session:
        return flask.render_template('login.html')

    user = application.user.services.fetch_by_email(session.email)
    if not user:
        flash_messages = [('danger', 'Invalid info while running verification')]
        return flask.render_template('login.html', flash_messages=flash_messages)

    verification_code = flask.request.args.get('verification_code')
    if verification_code != user.verification_code:
        return flask.render_template('index.html', user=user, not_verified=True)

    user = application.user.services.modify_user_validity(user.id, True)

    flash_messages = [('success', 'Verification successful!')] if user.verified else []
    return _set_session_and_get_response('index.html', user, not_verified=not user.verified, flash_messages=flash_messages)


@application.user.decorators.login_required
def verify_resend():
    session = application.core.session.get_session()
    if not session:
        return flask.render_template('login.html')

    user = application.user.services.fetch_by_email(session.email)
    if not user:
        return flask.render_template('login.html')

    application.user.mails.send_verification(user.email, user.first, user.verification_code)
    return flask.render_template('index.html', user=user, not_verified=True, resend=True)


def login_post():
    form = application.user.forms.UserLoginForm(csrf_enabled=False)

    if form.validate_on_submit():
        email = form.data.get('email')
        password = form.data.get('password')
        passhash = hashlib.md5(password).hexdigest()
        user = application.user.services.fetch_by_login(email, passhash)
        if user:
            return _set_session_and_get_response('index.html', user, not_verified=not user.verified)

        flash_messages = [('danger', 'Unable to Login')]
        return flask.render_template('login.html', flash_messages=flash_messages)

    flash_messages = [('warning', 'Invalid login!')]
    return flask.render_template('login.html', flash_messages=flash_messages)


def login_get():
    session = application.core.session.get_session()
    if not session:
        return _clear_session_and_get_response(flask.render_template('login.html'))

    user = application.user.services.fetch_by_email(session.email)
    if not user:
        return _clear_session_and_get_response(flask.render_template('login.html'))

    return _set_session_and_get_response('index.html', user, not_verified=not user.verified)


def _l(string):
    print '---%s' % string


def _set_session_and_get_response(html, user, **kwargs):
    response = flask.make_response(flask.render_template(html, user=user, **kwargs))
    sid = application.core.session.set_session(user.email)
    response.set_cookie('sid', sid)
    return response

import flask
import application.core.mails


def send_reset(email, first, reset_code):
    send_to = [email]
    subject = "Account reset instructions"

    data = {
        'first': first.capitalize(),
        'link': '%s?reset_code=%s&email=%s' % (flask.url_for('.reset', _external=True), reset_code, email)
    }

    body = """
    Hello %(first)s!

    To reset your account, please click on the link below.
    %(link)s

    If for some reason the link doesn't work, copy the link manually and visit the page.

    Regards
    """ % data

    html = body
    text = body

    application.core.mails.send_message(send_to, subject, html, text)


def send_verification(email, first, verification_code):
    send_to = [email]
    subject = "Required | Account verification instructions"

    data = {
        'first': first.capitalize(),
        'link': '%s?verification_code=%s' % (flask.url_for('.verify', _external=True), verification_code)
    }

    body = """
    Hello %(first)s!

    Thank you for registering! You are just one step away.

    Please click on the registration link below to complete your registration!

    %(link)s

    If for some reason the link doesn't work, copy the link manually and visit the page.

    Regards
    """ % data

    html = body
    text = body

    application.core.mails.send_message(send_to, subject, html, text)

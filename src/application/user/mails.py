import flask
import application.core.mails


def send_verification(email, first, verification_code):
    send_to = [email]
    subject = "Required | Account verification instructions"

    data = {
        'first': first.capitalize(),
        'link': flask.url_for('/verify', data={'verification_code': verification_code})
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

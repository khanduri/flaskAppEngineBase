import application.core.mails


def starter_email(send_to):

    subject = 'Sending with SendGrid is Fun'
    html = 'and easy to do anywhere, even with Python'
    text = 'Raw text content body'

    application.core.mails.send_message(send_to, subject, html, text)

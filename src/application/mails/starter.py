import application.mails

# TODO: think about async email trigger
# TODO: think about email priority


def starter_email(send_to):

    subject = 'Sending with SendGrid is Fun'
    html = 'and easy to do anywhere, even with Python'
    text = 'Raw text content body'

    application.mails.send_message(send_to, subject, html, text)

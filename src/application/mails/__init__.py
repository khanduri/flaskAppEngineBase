import sendgrid

import application.core.settings


email_provider = sendgrid.SendGridClient(
    application.core.settings.SENDGRID_USERNAME,
    application.core.settings.SENDGRID_PASSWORD,
    secure=True)


def send_message(send_to_list, subject, html, text, send_from=None):

    message = sendgrid.Mail()

    for send_to in send_to_list:
        message.add_to(send_to)
    message.set_subject(subject)
    message.set_html(html)
    message.set_text(text)

    if not send_from:
        message.set_from(application.core.settings.EMails.NO_REPLY)

    email_provider.send(message)

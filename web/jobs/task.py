from django.core.mail import send_mail

from src import settings


def enviar_correo_electronico(subject, message, recipient_list):
    print('dentroooooooooooo')
    send_mail(subject, '', settings.EMAIL_HOST_USER, recipient_list, html_message=message)

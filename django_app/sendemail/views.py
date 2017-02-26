from django.core.mail import send_mail
from django.http import HttpResponse

from sendemail import settings


def index(requset):

    send_mail(
        subject='Subject here',
        message='Here is the message.',
        from_email='woo95kil@gmail.com',
        recipient_list=['woo95kil@gmail.com'],
        auth_user=settings.EMAIL_USER_USER,
        auth_password=settings.EMAIL_USER_PASSWORD,
        # connection=config['email'][''],
    )

    return HttpResponse('complete')

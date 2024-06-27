from django.conf import settings
from django.core.mail import send_mail


def send_mail_for_registration(user, url):
    send_mail(
                'Подтверждение регистрации',
                f'Для подтверждения регистрации перейдите по ссылке {url}',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
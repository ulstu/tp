from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import Signal
from .utilities import send_activation_notification


class AdvUser(AbstractUser):
    phone = models.CharField(max_length=20, null=True, verbose_name="Номер телефона")
    patronymic = models.CharField(max_length=50, null=True,  verbose_name="Отчество")
    is_activated = models.BooleanField(default=True)
    send_messages = models.BooleanField(default=True, verbose_name='Слать оповещения о новых комментариях?')

    class Meta(AbstractUser.Meta):
        pass

user_registrated = Signal(providing_args=['instance'])


def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registrated.connect(user_registrated_dispatcher)

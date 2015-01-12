# coding: utf-8
from django.contrib import messages
from django.contrib.auth import user_logged_out
from registration import signals


def registered_notifier(user, request, **kwargs):
    messages.add_message(request, messages.INFO, u'Данные сохранены')


signals.user_registered.connect(registered_notifier)

def logout_notifier(sender, request, user, **kwargs):
    messages.info(request, u'Вы вышли')

user_logged_out.connect(logout_notifier)
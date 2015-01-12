# coding: utf-8
from django.contrib import messages
from registration import signals


def registered_notifier(user, request, **kwargs):
    messages.add_message(request, messages.INFO, u'Данные сохранены')


signals.user_registered.connect(registered_notifier)

# coding: utf-8
import logging
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login
from django.core.urlresolvers import reverse
from registration import signals
from registration.backends.simple.views import RegistrationView

User = get_user_model()

logger = logging.getLogger('project')

class CustomRegistrationView(RegistrationView):
    def register(self, request, **cleaned_data):
        email, password = cleaned_data.pop('email'), cleaned_data.pop('password')

        cleaned_data.pop('captcha')

        User.objects.create_user(email, email, password, **cleaned_data)

        new_user = authenticate(username=email, password=password)

        login(request, new_user)

        messages.add_message(request, messages.SUCCESS, u'Добро пожаловать!')

        signals.user_registered.send(sender=self.__class__, user=new_user, request=request)

        return new_user

    def get_success_url(self, request, user):
        return reverse('home')

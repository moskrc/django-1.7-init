# coding: utf-8
from django.contrib.auth.models import User, Group, Permission
from django.contrib.sites.models import Site

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

User = settings.AUTH_USER_MODEL


class CustomUser(AbstractUser):
    subscribe = models.BooleanField(u'Получать новости', default=True, blank=True)

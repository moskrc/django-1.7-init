# coding: utf-8
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from models import CustomUser
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'subscribe', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('last_name', 'first_name', 'email',
            'subscribe'

        )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
admin.site.register(CustomUser, CustomUserAdmin)

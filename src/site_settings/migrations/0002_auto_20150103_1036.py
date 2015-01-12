# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='analytics',
            field=models.CharField(default='', max_length=255, verbose_name=b'Analytics', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='description',
            field=models.CharField(default='', max_length=255, verbose_name=b'Description main', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='keywords',
            field=models.CharField(default='', max_length=255, verbose_name=b'Keywords main', blank=True),
            preserve_default=False,
        ),
    ]

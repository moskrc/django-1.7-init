# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0003_auto_20150103_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='analytics',
            field=models.TextField(max_length=4096, verbose_name=b'Analytics', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='counters',
            field=models.TextField(max_length=4096, verbose_name='\u0421\u0447\u0435\u0442\u0447\u0438\u043a\u0438', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='description',
            field=models.TextField(max_length=4096, verbose_name=b'Description main', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='header',
            field=models.TextField(max_length=2048, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='keywords',
            field=models.TextField(max_length=4096, verbose_name=b'Keywords main', blank=True),
            preserve_default=True,
        ),
    ]

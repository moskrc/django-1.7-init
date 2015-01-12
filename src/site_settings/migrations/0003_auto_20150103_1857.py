# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_auto_20150103_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='analytics',
            field=models.TextField(max_length=1024, verbose_name=b'Analytics', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='counters',
            field=models.TextField(max_length=2048, verbose_name='\u0421\u0447\u0435\u0442\u0447\u0438\u043a\u0438', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='description',
            field=models.TextField(max_length=1024, verbose_name=b'Description main', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='feedback_widget',
            field=models.TextField(max_length=2048, verbose_name='\u0412\u0438\u0434\u0436\u0435\u0442 \u043e\u0431\u0440\u0430\u0442\u043d\u043e\u0439 \u0441\u0432\u044f\u0437\u0438', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='footer',
            field=models.TextField(max_length=2048, verbose_name='\u041f\u043e\u0434\u0432\u0430\u043b', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='header',
            field=models.TextField(max_length=2048, verbose_name='111\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='intro',
            field=models.TextField(max_length=2048, verbose_name='\u0412\u0432\u0435\u0434\u0435\u043d\u0438\u0435 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='keywords',
            field=models.TextField(max_length=1024, verbose_name=b'Keywords main', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='meta_block',
            field=models.TextField(max_length=2048, verbose_name='\u0414\u043e\u043f. \u043c\u0435\u0442\u0430 \u0442\u0435\u0433\u0438', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='sub_header',
            field=models.TextField(max_length=2048, verbose_name='\u041f\u043e\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='top_left_block',
            field=models.TextField(max_length=2048, verbose_name='\u0412\u0435\u0440\u0445\u043d\u0438\u0439 \u043b\u0435\u0432\u044b\u0439 \u0431\u043b\u043e\u043a', blank=True),
            preserve_default=True,
        ),
    ]

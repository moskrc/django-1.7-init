# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_auto_20150103_0022'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430', blank=True)),
                ('email', models.CharField(max_length=255, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0439 email', blank=True)),
                ('email_order', models.CharField(max_length=255, verbose_name='Email \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0431\u0443\u0434\u0443\u0442 \u043e\u0442\u043f\u0440\u0430\u043b\u0432\u044f\u0442\u044c\u0441\u044f \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f \u043e \u0437\u0430\u043a\u0430\u0437\u0430\u0445', blank=True)),
                ('email_from', models.CharField(max_length=255, verbose_name='\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u044f\u0442\u044c \u043e\u0442', blank=True)),
                ('header', models.CharField(max_length=2048, verbose_name='111\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('sub_header', models.CharField(max_length=2048, verbose_name='\u041f\u043e\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('footer', models.CharField(max_length=2048, verbose_name='\u041f\u043e\u0434\u0432\u0430\u043b', blank=True)),
                ('intro', models.CharField(max_length=2048, verbose_name='\u0412\u0432\u0435\u0434\u0435\u043d\u0438\u0435 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439', blank=True)),
                ('logo', models.CharField(max_length=255, verbose_name='\u041f\u0443\u0442\u044c \u043a \u043b\u043e\u0433\u043e\u0442\u0438\u043f\u0443', blank=True)),
                ('logo_alt', models.CharField(max_length=255, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043b\u043e\u0433\u043e\u0442\u0438\u043f\u0430', blank=True)),
                ('search_button_alt', models.CharField(max_length=255, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u043d\u043e\u043f\u043a\u0438 \u043f\u043e\u0438\u0441\u043a\u0430', blank=True)),
                ('top_left_block', models.CharField(max_length=255, verbose_name='\u0412\u0435\u0440\u0445\u043d\u0438\u0439 \u043b\u0435\u0432\u044b\u0439 \u0431\u043b\u043e\u043a', blank=True)),
                ('feedback_widget', models.CharField(max_length=255, verbose_name='\u0412\u0438\u0434\u0436\u0435\u0442 \u043e\u0431\u0440\u0430\u0442\u043d\u043e\u0439 \u0441\u0432\u044f\u0437\u0438', blank=True)),
                ('meta_block', models.CharField(max_length=255, verbose_name='\u0414\u043e\u043f. \u043c\u0435\u0442\u0430 \u0442\u0435\u0433\u0438', blank=True)),
                ('google_maps_api_key', models.CharField(max_length=255, verbose_name='Google Maps API', blank=True)),
                ('yandex_maps_api_key', models.CharField(max_length=255, verbose_name='Yandex Maps API', blank=True)),
                ('google_analytics_id', models.CharField(max_length=255, verbose_name='Google Analytics ID', blank=True)),
                ('counters', models.CharField(max_length=255, verbose_name='\u0421\u0447\u0435\u0442\u0447\u0438\u043a\u0438', blank=True)),
                ('default_location_search', models.CharField(max_length=255, verbose_name='\u041f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 \u043f\u043e \u043a\u0430\u0440\u0442\u0435', blank=True)),
                ('city', models.ForeignKey(blank=True, to='notices.City', null=True)),
                ('site', models.ForeignKey(to='sites.Site', unique=True)),
            ],
            options={
                'verbose_name': '\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0430\u0439\u0442\u0430',
                'verbose_name_plural': '\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0430\u0439\u0442\u043e\u0432',
            },
            bases=(models.Model,),
        ),
    ]

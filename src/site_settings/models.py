# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.sites.models import Site
from notices.models import City


class SiteSettings(models.Model):
    site = models.ForeignKey(Site, unique=True)

    title = models.CharField(u'Название', max_length=255, blank=True)
    email = models.CharField(u'Контактный email', max_length=255, blank=True)
    email_order = models.CharField(u'Email на которые будут отпралвяться уведомления о заказах', max_length=255, blank=True)
    email_from = models.CharField(u'Отправлять от', max_length=255, blank=True)

    header = models.TextField(u'Заголовок', max_length=2048, blank=True)
    sub_header = models.TextField(u'Подзаголовок', max_length=2048, blank=True)
    footer = models.TextField(u'Подвал', max_length=2048, blank=True)
    intro = models.TextField(u'Введение на главной', max_length=2048, blank=True)
    logo = models.CharField(u'Путь к логотипу', max_length=255, blank=True)
    logo_alt = models.CharField(u'Текст логотипа', max_length=255, blank=True)
    search_button_alt = models.CharField(u'Текст кнопки поиска', max_length=255, blank=True)

    top_left_block = models.TextField(u'Верхний левый блок', max_length=2048, blank=True)
    feedback_widget = models.TextField(u'Виджет обратной связи', max_length=2048, blank=True)


    meta_block = models.TextField(u'Доп. мета теги', max_length=2048, blank=True)
    city = models.ForeignKey(City, blank=True, null=True)

    google_maps_api_key = models.CharField(u'Google Maps API',  max_length=255, blank=True)
    yandex_maps_api_key = models.CharField(u'Yandex Maps API', max_length=255, blank=True)
    google_analytics_id = models.CharField(u'Google Analytics ID', max_length=255, blank=True)

    keywords = models.TextField('Keywords main', max_length=4096, blank=True)
    description = models.TextField('Description main', max_length=4096, blank=True)
    analytics = models.TextField('Analytics', max_length=4096, blank=True)

    counters = models.TextField(u'Счетчики', max_length=4096, blank=True)

    default_location_search = models.CharField(u'По умолчанию текст для поиска по карте',  max_length=255, blank=True)


    class Meta:
        verbose_name = u'Настройки сайта'
        verbose_name_plural = u'Настройки сайтов'

    def __unicode__(self):
        return self.site.domain


# invoke settings to Site model
Site.get_settings = lambda self: self.sitesettings_set.filter(site=self).first() or SiteSettings(site=self)
Site.settings = property(Site.get_settings)

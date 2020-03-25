# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from corona_app.models import CoronaData

class CoronaScraperItem(DjangoItem):
    django_model = CoronaData

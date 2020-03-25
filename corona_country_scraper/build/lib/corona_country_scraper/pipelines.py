# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from corona_app.models import CountryData
from django.db import models

class CoronaCountryScraperPipeline(object):
    def process_item(self, item, spider):
        try:
            existatant = CountryData.objects.get(name=item['name'])
            existatant_id = existatant.id
            existatant = item.save(commit=False)
            existatant.id = existatant_id
            existatant.save()
        except models.ObjectDoesNotExist:
            item.save()
            
        # item.save()
        return item

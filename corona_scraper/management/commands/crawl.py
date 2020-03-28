from django.core.management.base import BaseCommand
from corona_scraper.spiders import corona.CoronaSpider

import os

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(CoronaSpider)
        print(os.getcwd())
        print('OK!')
# -*- coding: utf-8 -*-
import scrapy
import re
from corona_country_scraper.items import CoronaCountryScraperItem

def toInt(value):
    if value is None:
        return 0

    value = value.strip()
    value = re.sub("[^0-9]", "", value)
    value = value.replace(',', '')

    if value == " " or value == '':
        value = int(0)
    else:
        value = int(value)
    return value

def toFloat(value):
    if value is None:
        return 0.0

    value = value.strip()
    value = re.sub("[^0-9]", "", value)
    value = value.replace(',', '')
    value = float(value)
    return value

def tuneString(value):
    value = value.strip()
    value = re.sub("[^0-9]", "", value)
    return value

class CountrySpider(scrapy.Spider):
    name = 'country'
    start_urls = ['https://www.worldometers.info/coronavirus//']

    def parse(self, response):        
        tbody = response.xpath('//table[@id="main_table_countries_today"]/tbody')[0]
        trs = tbody.xpath('./tr')

        isProblem = False

        for tr in trs:
            try:
                item = CoronaCountryScraperItem()

                tds = tr.xpath('.//td')
                item = CoronaCountryScraperItem()

                country = tds[0].xpath('./text()').get()
                if country is None:
                    country = tds[0].xpath('.//a/text()').get()
                if country is None:
                    country = tds[0].xpath('.//span/text()').get()
                if country is None:
                    raise Exception('Error at Country name extraction')
                
                total_case = toInt(tds[1].xpath('./text()').get())
                new_case = toInt(tds[2].xpath('./text()').get())
                death = toInt(tds[3].xpath('./text()').get())
                new_death = toInt(tds[4].xpath('./text()').get())
                recovered = toInt(tds[5].xpath('./text()').get())
                active = toInt(tds[6].xpath('./text()').get())
                serious = toInt(tds[7].xpath('./text()').get())

                print("{} {} {} {} {} {} {} {}".format(country, total_case, new_case, death, new_death, recovered, active, serious))
                item['name'] = country
                item['total_case'] = total_case
                item['new_case'] = new_case
                item['death'] = death
                item['new_death'] = new_death
                item['recovered'] = recovered
                item['active'] = active
                item['serious'] = serious

                yield item
            except Exception as error:
                print("Error: {}".format(error))
                isProblem = True
        
        if isProblem:
            print("Error Happened During Crawling")
        else:
            print("Crawl Successfull!")

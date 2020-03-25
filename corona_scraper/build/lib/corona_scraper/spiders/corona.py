# -*- coding: utf-8 -*-
import scrapy
from corona_scraper.items import CoronaScraperItem

def parseMainData(response):
    try:
        item = CoronaScraperItem()

        div = response.css('#maincounter-wrap')
        key1 = div[0].xpath('.//h1/text()').get()
        key2 = div[1].xpath('.//h1/text()').get()
        key3 = div[2].xpath('.//h1/text()').get()
        key1 = key1.strip()
        key2 = key2.strip()
        key3 = key3.strip()
        print(key1)
        print(key2)
        print(key3)
        # Deaths:
        # Recovered:
        if key1 == 'Coronavirus Cases:':
            value = div[0].xpath('.//div[@class="maincounter-number"]/span/text()').get()
            value = value.strip()
            value = value.replace(',','')
            value = int(value)
            print("{} {} {}".format(key1, value, type(value)))

            item['total_case'] = value
        else:
            raise Exception('error')
        
        if key2 == 'Deaths:':
            value = div[1].xpath('.//div[@class="maincounter-number"]/span/text()').get()
            value = value.strip()
            value = value.replace(',','')
            value = int(value)
            print("{} {} {}".format(key1, value, type(value)))

            item['death'] = value
        else:
            raise Exception('error')

        if key3 == 'Recovered:':
            value = div[2].xpath('.//div[@class="maincounter-number"]/span/text()').get()
            value = value.strip()
            value = value.replace(',','')
            value = int(value)
            print("{} {} {}".format(key1, value, type(value)))

            item['recovered'] = value
        else:
            raise Exception('error')

        yield item

        print('Crawl Successfull!')
    except:
        print('error occured')

def toInt(value):
    value = value.strip()
    value = value.replace(',', '')
    value = int(value)

    return value

def toFloat(value):
    value = value.strip()
    value = value.replace(',', '')
    value = float(value)
    return value


class CoronaSpider(scrapy.Spider):
    name = 'corona'
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        item = CoronaScraperItem()        
        try:
            item = CoronaScraperItem()

            div = response.css('#maincounter-wrap')

            key1 = div[0].xpath('.//h1/text()').get()
            key2 = div[1].xpath('.//h1/text()').get()
            key3 = div[2].xpath('.//h1/text()').get()
            key1 = key1.strip()
            key2 = key2.strip()
            key3 = key3.strip()
            print(key1)
            print(key2)
            print(key3)

            if key1 == 'Coronavirus Cases:':
                value = div[0].xpath('.//div[@class="maincounter-number"]/span/text()').get()
                value = value.strip()
                value = value.replace(',','')
                value = int(value)
                print("{} {} {}".format(key1, value, type(value)))

                item['total_case'] = value
            else:
                raise Exception('error')
            
            if key2 == 'Deaths:':
                value = div[1].xpath('.//div[@class="maincounter-number"]/span/text()').get()
                value = value.strip()
                value = value.replace(',','')
                value = int(value)
                print("{} {} {}".format(key2, value, type(value)))

                item['death'] = value
            else:
                raise Exception('error')

            if key3 == 'Recovered:':
                value = div[2].xpath('.//div[@class="maincounter-number"]/span/text()').get()
                value = value.strip()
                value = value.replace(',','')
                value = int(value)
                print("{} {} {}".format(key3, value, type(value)))

                item['recovered'] = value
            else:
                raise Exception('error')
            
            div = response.css('.panel.panel-default')

            key1 = div[0].xpath('.//div[@class="panel-heading"]/span/text()').get()
            key2 = div[1].xpath('.//div[@class="panel-heading"]/span/text()').get()
            key1 = key1.strip()
            key2 = key2.strip()
            key1 = key1.lower()
            key2 = key2.lower()

            if(key1 == 'active cases'):
                # .panel-body .panel_flip .panel_front .number-table-main
                activeCaseValue = div[0].xpath('.//div[@class="panel-body"]//div[@class="panel_flip"]//div[@class="panel_front"]//div[@class="number-table-main"]/text()').get()
                activeCaseValue = activeCaseValue.strip()
                activeCaseValue = activeCaseValue.replace(',', '')
                activeCaseValue = int(activeCaseValue)

                item['active'] = activeCaseValue
                print("{} {} {}".format(key1, activeCaseValue, type(activeCaseValue)))

                middleDiv = div[0].xpath('.//div[@class="panel-body"]//div[@class="panel_flip"]//div[@class="panel_front"]//div/span')
                mildCondition = middleDiv[0].xpath('./text()').get()
                seriousCondition = middleDiv[1].xpath('./text()').get()

                middleDivPercentage = div[0].xpath('//div[@class="panel-body"]//div[@class="panel_flip"]//div[@class="panel_front"]//div/strong')
                mildConditionPercentage = middleDivPercentage[0].xpath('./text()').get()
                seriousConditionPercentage = middleDivPercentage[1].xpath('./text()').get()

                item['mild'] = toInt(mildCondition)
                item['serious'] = toInt(seriousCondition)
                item['mild_percentage'] = toFloat(mildConditionPercentage)
                item['serious_percentage'] = toFloat(seriousConditionPercentage)

            else:
                raise Exception('active case error')

            if(key2 == 'closed cases'):
                closedCaseValue = div[1].xpath('.//div[@class="panel-body"]//div[@class="panel_flip"]//div[@class="panel_front"]//div[@class="number-table-main"]/text()').get()
                item['closed'] = toInt(closedCaseValue)

                middleDivPercentage = div[1].xpath('.//div[@class="panel-body"]//div[@class="panel_flip"]//div[@class="panel_front"]//div/strong')
                recoverdOrDischargesPercentage = middleDivPercentage[0].xpath('./text()').get()
                deathPercentage = middleDivPercentage[1].xpath('./text()').get()

                item['recovered_or_discharged_percentage'] = toFloat(recoverdOrDischargesPercentage)
                item['death_percentage'] = toFloat(deathPercentage)
            else:
                raise Exception('closed case error')

            yield item
            print('Crawl Successfull!')
        except Exception as error:
            print("Error: {}".format(error))
    
    
# -*- coding: utf-8 -*-

import scrapy


class UrlItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()


class CarItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    o_price = scrapy.Field()
    miles = scrapy.Field()
    buy_date = scrapy.Field()
    level = scrapy.Field()
    output = scrapy.Field()
# -*- coding: utf-8 -*-
import scrapy


class JdItem(scrapy.Item):
    book_dict = scrapy.Field()


class Url_Item(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
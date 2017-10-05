# -*- coding: utf-8 -*-
import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    sco = scrapy.Field()
    title = scrapy.Field()
    act = scrapy.Field()
    pic = scrapy.Field()
    link = scrapy.Field()

#糗事百科段子内容。好笑数、评论数、正文。
class QiushiItem(scrapy.Item):
    good = scrapy.Field()
    comment = scrapy.Field()
    text = scrapy.Field()

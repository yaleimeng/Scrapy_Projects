# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem

class FilmSpider(scrapy.Spider):
    name = 'film'
    allowed_domains = ['kan.2345.com']
    start_urls = ['http://kan.2345.com/vip/list/--movie--0---{}.html'.format(str(i))   for i in range(1,101)]

    def parse(self, response):
        dys = response.xpath('.//*[@id = "contentList"] //li')
        for dy in dys:   #针对每个目标区域，抽取需要的内容
            atitle = dy.xpath('.//*[@class = "pic"]/img/@alt').extract()[0]
            aact   = dy.xpath('.//*[@class = "sActor"]/em/a/text()').extract()
            actors = ''
            for ac in aact:
                actors += ac    #把多个主演连接起来。
            actors = actors[:-2].replace('\xa0\xa0','、')
            asco   = dy.xpath('.//*[@class = "emScore"]/text()').extract()[0]
            apic   = 'http:'+dy.xpath('.//*[@class = "pic"]/img/@data-src').extract()[0]
            alink  = dy.xpath('.//*[@class = "emTit"]/a/@href').extract()[0]

            print(atitle,'\t',aact,'\t',asco,'\t',apic,'\t',alink,'\n')
            item = MovieItem( title = atitle,    act = actors, sco = asco,
                              pic  = apic,    link = alink)
            yield item   #提交Item

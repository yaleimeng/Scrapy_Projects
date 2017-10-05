# -*- coding: utf-8 -*-
import scrapy
from YouXin.items import UrlItem

class UrlsSpider(scrapy.Spider):
    name = 'urls'
    allowed_domains = ['xin.com']
    # URL的第一个参数是地区，可以修改为其他城市。
    start_urls = ['https://www.xin.com/{}/sn_t1000/i{}'.format('suzhou',str(i)) for i in range(1,51)]

    def parse(self, response):
        out = response.css('li.con div.pad a')
        host = 'https://www.xin.com'
        for o in out:
            url = host+o.xpath('./@href').extract_first()[:-8]
            print (url)
            item = UrlItem(link = url )
            yield item

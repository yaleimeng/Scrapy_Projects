# -*- coding: utf-8 -*-
import scrapy
from JD.items import Url_Item

class UrlSpider(scrapy.Spider):
    name = 'JDurl'
    allowed_domains = ['jd.com','360buy.com']
    start_urls = ['https://list.jd.com/list.html?cat=1713,3287,3797&page={}&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main'
                  .format(str(n)) for n in range(1,246)]
    #这里获取的是【编程语言与程序设计】分类下的所有图书。245页。

    def parse(self, response):
      books = response.css('li.gl-item div.p-name > a')
      for book in books:
          item = Url_Item(name = book.css('em::text').extract()[0].replace(' ','')[1:] ,
                          url  = 'http:'+book.css('::attr(href)').extract()[0] )
          print(item)
          yield item
#
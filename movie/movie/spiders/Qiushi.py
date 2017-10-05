# -*- coding: utf-8 -*-
import scrapy
from movie.items import QiushiItem

class QiushiSpider(scrapy.Spider):
    name = 'Qiushi'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,14)]

    def parse(self, response):
        jokes = response.xpath('.//*[@id = "content-left"]/div')
        for jk in jokes:  # 针对每个目标区域，抽取需要的内容
            up = jk.xpath('.//*[@class = "stats-vote"]/i/text()').extract()[0]
            cmt = jk.xpath('.//*[@class = "stats-comments"]//i/text()').extract()[0]
            content = jk.xpath('.//a/div/span/text()').extract()[0].replace('\n','')  #去掉多余的换行。
            print(up, '\t', cmt, '\t',  content, '\n')  #打印当前信息
            item = QiushiItem( good = up,    comment =cmt,    text =content)
            yield item  # 提交Item
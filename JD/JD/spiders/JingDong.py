# -*- coding: utf-8 -*-
import scrapy
import json
import requests as rq
from JD.items import JdItem

class JingdongSpider(scrapy.Spider):
    name = 'JingDong'
    allowed_domains = ['jd.com','360buy.com','p.3.cn']
    start_urls = []
    with open('E:/ProBook.txt', 'r', encoding='utf-8')as f:
        for line in f.readlines():         # 按整行依次读取数据。
            link = line.replace("\n", '')  # 把回车符号替换为空。这样网址就是可访问的。
            if link not in start_urls:     # 写入时无法检查，读取时要防止URL重复。
                start_urls.append(link)

    def parse(self, response):
        name = response.xpath('//div[@id="name"]/h1/text()').extract_first().replace(' ', '')
        data = response.xpath('//div[@id="p-author"]')
        author = data.xpath('string(.)').extract_first().replace('\n','').replace(' ', '')
        data = response.xpath('//ul[@id="parameter2"]')
        detail = data.xpath('string(.)').extract_first()[1:-1].replace(' ', '')
        shop = '京东自营'  if detail[:3] == '出版社' else response.xpath('//ul[@id="parameter2"]/li[1]/a/text()').extract_first()
        book_id = response.xpath('//head/link/@href').extract_first().split('/')[-1].split('.')[0]
        this = 'http:'+response.xpath('//head/link/@href').extract_first()   #本页的url
        #因为价格与评论信息是发起JS请求，从响应中提取JSON数据，所以不再利用scrapy内置功能。自己Requests
        jsurl = 'http://p.3.cn/prices/get?type=1&area=1_72_2799&ext=11000000&pin=&' \
                'pdtk=FPccakpV9mj2W7jFSF%2BtATks2rbgJDLiwIUI5nkedHiAWTgr9wJVrXOToICN%2B93%2B&' \
                'pduid=1506124005948838590885&pdpin=&pdbp=0&skuid=J_{}&callback=cnp'.format(book_id)
        #pdtk是 Cookie的最后一段。想办法动态获得。
        str = self.getJsonFrom(jsurl).text[5:-4]    #去掉前后部分才是JSON格式
        price = json.loads(str)       #获取json数据。
        cmturl = 'http://club.jd.com/comment/productCommentSummaries.action?referenceIds={}'.format(book_id)
        info = self.getJsonFrom(cmturl).json()
        Item = JdItem( book_dict =
                       {'书名': name,   '作者': author,  '店铺': shop ,   '现价': float(price['p']), '定价': float(price['m']),
                        '平常价': float(price['op']),    '评论数': int(info['CommentsCount'][0]['CommentCount']),
                        '好评率': float(info['CommentsCount'][0]['GoodRate']),   '详情': detail,  '链接': this       } )
        yield Item


    def getJsonFrom(self,page):
        head = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                              ' Chrome/62.0.3192.0 Safari/537.36'}
        r = rq.get(page, headers = head, timeout = 5)
        return r
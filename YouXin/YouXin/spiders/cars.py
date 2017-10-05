# -*- coding: utf-8 -*-
import scrapy
from YouXin.items import CarItem

class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['xin.com']
    start_urls = []
    with open('E:/youxin.txt', 'r', encoding='utf-8')as f:
        for line in f.readlines():  # 按整行依次读取数据。
            link = line.replace("\n", '')  # 把回车符号替换为空。这样网址就是可访问的。
            if link not in start_urls:  # 写入时无法检查，读取时要防止URL重复。
                start_urls.append(link)

    def parse(self, response):
        car_name = response.xpath("//div[@class = 'cd_m_info_it2']/div[1]/span/text()").extract_first()
        car_pri  = response.xpath("//div[@class = 'cd_m_info_it2']/p[1]/span[1]/b/text()").extract_first()[1:-1]
        o_pri = response.xpath("//div[@class = 'cd_m_info_it2']/p[1]/span[2]/text()").extract_first()[2:-5]
        distance = response.xpath("//div[@class = 'cd_m_info_it2']/table/tr[1]/td[1]/span[1]/a/text()").extract_first().strip()
        buy_month = response.xpath("//div[@class = 'cd_m_info_it2']/table/tr[1]/td[2]/span[1]/text()").extract_first()
        out_level = response.xpath("//div[@class = 'cd_m_info_it2']/table/tr[2]/td[1]/span[1]/text()").extract_first()
        pai_liang = response.xpath("//div[@class = 'cd_m_info_it2']/table/tr[2]/td[2]/span[1]/text()").extract_first()
        #print(car_name,car_pri,o_pri,distance,buy_month,out_level,pai_liang,sep='\n')
        item = CarItem(name = car_name,price = float(car_pri),o_price = float(o_pri),miles = distance,
                       buy_date = buy_month,           level = out_level,output = pai_liang)
        yield item
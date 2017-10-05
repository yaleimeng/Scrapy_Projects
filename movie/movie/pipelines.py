# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
from scrapy.exceptions import DropItem
class MoviePipeline(object):
    def __init__(self):
        self.f = open('E:/movie.csv','a',encoding='utf-8')


    def process_item(self, item, spider):
        if item['name']:
            wr = csv.writer(self.f)
            wr.writerow(item)
            return item
        else:
            raise DropItem('Misssing name in %s'%item)


# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
import pymongo as mg

class JdPipeline(object):   #从图书详情页收集书名、作者、价格、出版社、评论数等信息的管道，写入MongoDB数据库。
    def __init__(self):
        client = mg.MongoClient('localhost', 27017)
        JD = client['JingDong']          # 设定要操作的数据库。=左边是python变量名，中括号里是MongoDB数据库名。
        self.proBook = JD['ProgramBook']  # 设定要操作的数据表。=左边是python用的变量名，中括号里面是数据表名。

    def process_item(self, item, spider):
        if item['book_dict']['书名'] and item['book_dict']['作者'] :
            self.proBook.insert_one(item['book_dict'])
            print('\n数据库当前已有  %d  条数据。\n'%self.proBook.count())
            return item
        else:
            raise DropItem('%s这一条没有 书名/作者 属性，已丢弃！'%item)


class UrlPipeline(object):    #这是从各列表页面收集URL信息的管道。
    def __init__(self):
        self.f = open('E:/ProBook.txt', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        if item['url']:
            self.f.write(item['url'])
            self.f.write('\n')
            return item
        else:
            raise DropItem('%s这一条没有 url 属性！' % item)

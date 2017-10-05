# -*- coding: utf-8 -*-
import csv

class UrlPipeline(object):

    def process_item(self, item, spider):
        with open('E:/youxin.txt', 'a', encoding='utf-8') as f:
            if item['link']:
                f.write(item['link'])
                f.write('\n')
        return item


class CarPipeline(object):

    def process_item(self, item, spider):
        with open('E:/youxin.csv', 'a', encoding='utf-8') as f:
            if item['name']:
                fw = csv.writer(f)
                row = [item['name'],item['price'],item['o_price'],item['miles'],
                       item['buy_date'],item['level'],item['output'] ]
                fw.writerow(row)
        return item
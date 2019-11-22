# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import pymysql

class Ershouche58Pipeline(object):
    # def process_item(self, item, spider):
    #     print("开始执行了。。。。")
    #     f = open('data_beijing.csv', 'a+', encoding='utf-8')
    #     writer = csv.writer(f)
    #     writer.writerow(['brand', 'title', 'start_time', 'distance', 'volumn', 'gear', 'tag', 'price'])
    #     return item
    '''
     1、数据存储到 csv 文件中
    '''
    def __init__(self):
        # 打开文件，指定方式为写，利用第3个参数把csv写数据时产生的空行消除
        self.f = open("data_beijing.csv", "w", newline="")
        # 设置文件第一行的字段名，注意要跟spider传过来的字典key名称相同
        self.fieldnames = ['city','brand', 'title', 'start_time', 'distance', 'volumn', 'gear', 'tag', 'price']
        # 指定文件的写入方式为csv字典写入，参数1为指定具体文件，参数2为指定字段名
        self.writer = csv.DictWriter(self.f, fieldnames=self.fieldnames)
        # 写入第一行字段名，因为只要写入一次，所以文件放在__init__里面
        self.writer.writeheader()

    def process_item(self, item, spider):
        # 写入spider传过来的具体数值
        # 字段的形式遍历输出 item 数据
        for j in range(len(item['brand'])):
            self.writer.writerow({'city':item['city'],'brand': item['brand'][j], 'title': item['title'][j],
                                  'start_time': item['start_time'][j], 'distance': item['distance'][j],
                                  'volumn': item['volumn'][j],'gear':item['gear'][j], 'tag': item['tag'][j], 'price': item['price'][j]})
        # 写入完返回
        return item

    def close(self, spider):
        self.f.close()






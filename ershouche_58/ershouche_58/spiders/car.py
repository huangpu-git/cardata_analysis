# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Selector
from time import sleep

class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['bj.58.com/ershouche']
    start_template = 'https://{}.58.com/ershouche/pn{}/'

    # start_urls = [start_template.format('1')]

    def start_requests(self):
        city_list=['bj','sh','gz','sz','hz']
        for city in city_list:
            for page in range(1, 100):
                start_urls = self.start_template.format(city,page)
                yield scrapy.Request(start_urls, callback=self.parse)

    def parse(self, response):
        city = response.xpath(".//div[@class='tab_lists clearfix']/ul/li/a[@class='tab_active']/text()").get()
        brand = response.xpath(".//ul[@class='car_list ac_container']/li/div/a/h1/font/text()").getall()
        title = response.xpath(".//ul[@class='car_list ac_container']/li/div/a[@class='ac_linkurl']/h1[1]/text()").re(
            "(\S+.+\S)")
        start_time = response.xpath(".//ul[@class='car_list ac_container']/li/div/div/span[1]/text()").getall()
        distance = response.xpath(".//ul[@class='car_list ac_container']/li/div/div/span[2]/text()").getall()
        volumn = response.xpath(".//ul[@class='car_list ac_container']/li/div/div/span[3]/text()").getall()
        gear = response.xpath(".//ul[@class='car_list ac_container']/li/div/div/span[4]/text()").getall()
        tag = response.xpath(".//ul[@class='car_list ac_container']/li/div/div/div/em/text()").getall()
        price = response.xpath(".//ul[@class='car_list ac_container']/li/div[3]/h3/text()").getall()
        yield {
            'city':city,
            'brand': brand,
            'title': title,
            'start_time': start_time,
            'distance': distance,
            'volumn': volumn,
            'gear': gear,
            'tag': tag,
            'price': price,
        }

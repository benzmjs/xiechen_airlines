# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XichenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hangxian_name = scrapy.Field()
    qifeidaoda = scrapy.Field()
    jichang = scrapy.Field()
    hangkonggonsi = scrapy.Field()
    hangbanhao = scrapy.Field()

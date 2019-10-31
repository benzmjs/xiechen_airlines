# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook


class XichenPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['航线名称', '起飞时间', '到达时间', '起飞机场', '到达机场', '航空公司','航班号'])

    def process_item(self, item, spider):
        line=[item["hangxian_name"],item["qifeidaoda"][0],item["qifeidaoda"][1],item["jichang"][0],item["jichang"][1],item["hangkonggonsi"][0],item["hangbanhao"][0]]
        self.ws.append(line)
        print(item["hangxian_name"],item["qifeidaoda"][0],item["qifeidaoda"][1],item["jichang"][0],item["jichang"][1],item["hangkonggonsi"][0],item["hangbanhao"][0])
        self.wb.save('xiecheng.xlsx')
        return item

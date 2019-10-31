# -*- coding: utf-8 -*-
import scrapy
from xichen.items import XichenItem


class HangbanSpider(scrapy.Spider):
    name = 'hangban'
    allowed_domains = ['flights.ctrip.com']
    start_urls = ['https://flights.ctrip.com/schedule/het-outmap.html']

    def parse(self, response):
        item = XichenItem()
        all_info_list = response.xpath('//*[@id="flt1"]/tr')
        for every_info in all_info_list:
            item["hangxian_name"] = every_info.xpath('td/a[1]/text()').extract_first()
            item["qifeidaoda"] = [x.strip() for x in every_info.xpath('td[2]/text()').extract() if x.strip() != '']
            item["jichang"] = [x.strip() for x in every_info.xpath('td[3]/text()').extract() if x.strip() != '']
            item["hangkonggonsi"] = [x.strip() for x in every_info.xpath('td[7]/text()').extract() if x.strip() != '']
            item["hangbanhao"] = [x.strip() for x in every_info.xpath('td[7]/a/text()').extract() if x.strip() != '']
            yield item
        next_url = response.xpath('//*[@id="base_bd"]/div[3]/div/div/div/a[2]/@href').extract()
        if next_url != 'javascript:void(0)':
            yield scrapy.Request(
                next_url[0],
                callback=self.parse,
            )

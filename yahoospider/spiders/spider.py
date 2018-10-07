# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import YahoospiderItem
from scrapy.contrib.exporter import JsonItemExporter


class SpiderSpider(CrawlSpider):
    name = 'yahoo_spider'
    start_urls = ['https://tw.buy.yahoo.com/help/helper.asp?p=sitemap']
    # start_urls = ['https://tw.buy.yahoo.com/?catitemid=40503&sort=-tsales&pg=1']

    rules = (
		Rule(LinkExtractor(allow=('/?sub=\d+')), follow=True),
		Rule(LinkExtractor(allow=('/?catitemid=\d+')), follow=True),
		Rule(LinkExtractor(allow=('/?catitemid=\d+&sort=-tsales&pg=\d+')), callback='parse_item',follow=True),
    )
	
    # def parse(self, response):
    def parse_item(self, response):
		cat1 = response.xpath('//meta/@data-cat1').extract()
		cat2 = response.xpath('//meta/@data-cat2').extract()
		cat3 = response.xpath('//meta/@data-cat3').extract()
		cat4 = response.xpath('//meta/@data-cat4').extract()
		pid  = response.xpath('//*[@id="srp_result_list"]//div[contains(@class, "item")]/@data-pid').extract()
		pdprice = response.xpath('//*[@id="srp_result_list"]//div[contains(@class, "srp-pdprice")]//div[1]//span[2]/text()').extract()
		item = YahoospiderItem()
		for i in range(0, len(pid)):
			item['cat1']  = cat1[0]
			item['cat2']  = cat2[0]
			item['cat3']  = cat3[0]
			item['cat4']  = cat4[0]
			item['pid']   = pid[i]
			item['price'] = pdprice[i]
			yield item
		
		

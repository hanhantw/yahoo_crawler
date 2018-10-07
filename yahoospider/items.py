# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YahoospiderItem(scrapy.Item):
	cat1 = scrapy.Field()
	cat2 = scrapy.Field()
	cat3 = scrapy.Field()
	cat4 = scrapy.Field()
	pid  = scrapy.Field()
	price = scrapy.Field()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class YahoospiderPipeline(object):
    def __init__(self):
        self.file = open('bestseller.json', mode='w')

    def process_item(self, item, spider):
        jsondata = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(jsondata)
        return item

    def close_spider(self, spider):
        self.file.close()

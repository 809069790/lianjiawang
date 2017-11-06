# -*- coding: utf-8 -*-
import json
import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LianjiawangPipeline(object):
    def process_item(self, item, spider):
        with codecs.open('lianjiawang.json', 'a', encoding='utf-8') as f:
            line = json.dumps(list(item), ensure_ascii=False)
            f.write(line)
        return item

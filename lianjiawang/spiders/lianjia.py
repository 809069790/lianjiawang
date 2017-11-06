# -*- coding: utf-8 -*-
import scrapy
# from scrapy.http import Request
from lianjiawang.items import LianjiawangItem

class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["https://bj.lianjia.com/zufang/"]
    # 我这里只获取了两页，修改范围即可
    start_urls = ['https://bj.lianjia.com/zufang/pg'+ str(index) +'/' for index in range(1,3)]

    def parse(self, response):
        # 获取所有的li
        item = LianjiawangItem()
        all_li = response.xpath('.//ul[@class="house-lst"]//li')
        for li in all_li:
            item['des'] = li.xpath('.//div[@class="info-panel"]/h2/a/text()').extract()[0]
            price_1 = li.xpath('.//div[@class="info-panel"]/div[@class="col-3"]//span/text()').extract()[0]
            price_2 = li.xpath('.//div[@class="price"]/text()').extract()[0]
            item['price'] = price_1 + price_2
            pattern = li.xpath('.//div[@class="info-panel"]//div[@class="where"]/span/span/text()').extract()[0].strip()
            size = li.xpath('.//div[@class="info-panel"]//div[@class="where"]/span[@class="meters"]/text()').extract()[0].strip()
            item['size'] = pattern + size
            item['address'] = li.xpath('.//div[@class="info-panel"]//div[@class="where"]/a/span/text()').extract()[0].strip()
            yield item



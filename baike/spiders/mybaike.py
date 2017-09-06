# -*- coding: utf-8 -*-
import scrapy
from baike.items import BaikeItem


class MybaikeSpider(scrapy.Spider):
    name = 'mybaike'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/article/119494971']
    # for i in xrange(119494971, 119494991):
    #     url = 'http://www.qiushibaike.com/article/' + str(i) + '/'
    #     # start_urls = ['http://www.qiushibaike.com/']
    #     start_urls.append(url)

    def parse(self, response):
        subSelector = response.xpath('//div[@class="article block untagged noline mb15" and @id]')
        items = []
        for sub in subSelector:
            item = BaikeItem()
            item['author'] = sub.xpath('.//h2/text()').extract()[0]
            item['content'] = sub.xpath('.//div[@class="content"]/text()').extract()[0]
            item['img'] = sub.xpath('.//img/@src').extract()
            item['funNum'] = sub.xpath('.//i[@class="number"]/text()').extract()[0]
            try:
                item['talkNum'] = sub.xpath('.//i[@class="number"]/text()').extract()[1]
            except IndexError:
                item['talkNum'] = '0'
            items.append(item)
        return items

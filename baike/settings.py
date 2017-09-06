# -*- coding: utf-8 -*-

# Scrapy settings for baike project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'baike'

SPIDER_MODULES = ['baike.spiders']
NEWSPIDER_MODULE = 'baike.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'baike (+http://www.yourdomain.com)'
from baike.middlewares.customMiddlewares import CustomUserAgent
# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
DOWNLOADER_MIDDLEWARES = {
    # 'qiushi.middlewares.customMiddlewares.CustomProxy': 10,
    'baike.middlewares.customMiddlewares.CustomUserAgent': 3,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 20
}
ITEM_PIPELINES = {
    'baike.pipelines.BaikePipeline': 10,
}
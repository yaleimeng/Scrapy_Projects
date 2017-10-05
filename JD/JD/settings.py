# -*- coding: utf-8 -*-
import random

BOT_NAME = 'JD'

SPIDER_MODULES = ['JD.spiders']
NEWSPIDER_MODULE = 'JD.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3192.0 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = random.uniform(0.8,1.9)

# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 30
CONCURRENT_REQUESTS_PER_IP = 30

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

#Configure item pipelines   #必要的时候进行切换。
#ITEM_PIPELINES = {   'JD.pipelines.JdPipeline': 300,        }
#ITEM_PIPELINES = {   'JD.pipelines.UrlPipeline': 300,       }


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'JD.middlewares.JDSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'JD.middlewares.JDDownloaderMiddleware': 543
# }

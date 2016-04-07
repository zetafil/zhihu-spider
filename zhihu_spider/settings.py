# -*- coding: utf-8 -*-

# Scrapy settings for zhihu_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu_spider'

SPIDER_MODULES = ['zhihu_spider.spiders']
NEWSPIDER_MODULE = 'zhihu_spider.spiders'

# MONGO_URI='mongodb://127.0.0.1:27017'
MONGO_URI='mongodb://127.0.0.1:8100'
MONGO_DATABASE='zhihu'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu_spider (+http://www.yourdomain.com)'
USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=.1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
'Cookie': '_za=44adbaf5-d84b-4642-9ed7-f9ea277e7d45; udid="AGBAvxk3lQmPTiEWuCKqzZj2d1eGXwVa97A=|1457503823"; d_c0="AJDA4kYkogmPTqjcdrH55c1UiT-ehjAaCj4=|1458279968"; _xsrf=1177029a662946153628dd613bbb4a89; _ga=GA1.2.2049539814.1432119670; __utmt=1; q_c1=61c06c40a04b4281bc6f0903ba798405|1460006067000|1460006067000; l_cap_id="Y2I1NDYyMWNiOGRlNGU4YmE2NTNjYmQxNzY1NjA3NTA=|1460006067|a7184f0552182690fd4f0037b75a0995580ad44a"; cap_id="M2ZlMzQ5YTM1M2RkNDJjOGJhMjU3ZTQyODBhYTc4NTk=|1460006067|a16c2ae0fdfd190fa3551ab39f0eac4de875b6f0"; login="MWI4YjkxMWE0MWI2NGU3NTliNzc5MTY3MTZmYzI1Njg=|1460006132|1d036d203c70f65b5c1e84574efc48803b151aba"; z_c0="QUFCQUZya1lBQUFYQUFBQVlRSlZUZng1TFZkZVZpT0VNdUJWMEhUV2pwX0xFYWlnQW1neTlRPT0=|1460006141|13ad319f7039d68d9acf94ff60481afeee27c644"; unlock_ticket="QUFCQUZya1lBQUFYQUFBQVlRSlZUUVQwQlZlSG1Ndk12TmIyLUhLSHM2SFJSTUdVREs0ZThBPT0=|1460006141|7a6adba63d9c345b5e904232c1e8adbffe4de54f"; n_c=1; __utma=51854390.2049539814.1432119670.1459999277.1460006052.6; __utmb=51854390.6.10.1460006052; __utmc=51854390; __utmz=51854390.1459947564.4.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=51854390.100-1|2=registration_date=20111017=1^3=entry_date=20111017=1',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu_spider.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'zhihu_spider.middlewares.MyCustomDownloaderMiddleware': 543,
   'scrapy.contrib.spidermiddleware.httperror.HttpErrorMiddleware': 543,
   'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 500,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
EXTENSIONS = {
   'scrapy.telnet.TelnetConsole': None,
   'scrapy.extensions.closespider.CloseSpider': 500,
}
# CLOSESPIDER_PAGECOUNT = 10000

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#    'zhihu_spider.pipelines.SomePipeline': 300,
   'zhihu_spider.pipelines.DuplicatesPipeline': 300,
   'zhihu_spider.pipelines.MongoPipeline': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'

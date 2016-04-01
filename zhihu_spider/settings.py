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
DOWNLOAD_DELAY=1
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
'Cookie': 'Cookie: _za=44adbaf5-d84b-4642-9ed7-f9ea277e7d45; cap_id="Zjc4NDdjODA0YTViNGIzZDk3ODNjZTE1MjQyZDgzNDk=|1457412486|b84781fc6ceaec9da3c5167f657e8945e39f2ece"; z_c0="QUFCQUZya1lBQUFYQUFBQVlRSlZUWkRtQlZmQ09WVmJSemtkWU50dlpzTVVDSkRvRWltQjRRPT0=|1457412496|d69dded4732afbda4d7be5045ba9761b21d2f3cb"; udid="AGBAvxk3lQmPTiEWuCKqzZj2d1eGXwVa97A=|1457503823"; d_c0="AJDA4kYkogmPTqjcdrH55c1UiT-ehjAaCj4=|1458279968"; q_c1=9137111e22384722bec3bb1a7fc74b88|1458484741000|1429880911000; _xsrf=1177029a662946153628dd613bbb4a89; _ga=GA1.2.2049539814.1432119670; __utmt=1; __utma=51854390.2049539814.1432119670.1459489024.1459489024.1; __utmb=51854390.10.10.1459489024; __utmc=51854390; __utmz=51854390.1459489024.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20111017=1^3=entry_date=20111017=1',
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

# -*- coding: utf-8 -*-
import scrapy
import json
import urllib
from urlparse import urlparse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pprint import pprint
from scrapy.selector import Selector
import re
class PeopleSpider(CrawlSpider):
    name = 'people'
    allowed_domains = ['www.zhihu.com']
    handle_httpstatus_list = [403]

    start_urls = [
    # 'https://www.zhihu.com/explore',
    # 'https://www.zhihu.com/topics',
    'https://www.zhihu.com/people/zhi-shi-jiu-shi-li-liang-13',
    ]

    rules = (
        Rule(LinkExtractor(allow=('zhihu\.com/question/', 'zhihu\.com/topic/'))),

        Rule(LinkExtractor(allow=('zhihu\.com/people/')), callback='parse_item'),
    )

    def parse_item(self, response):
        # self.log('Hi, this is an item page! %s' % response.url)
        # print 'parse_item: '+response.url
        # item = SportItem()
        # item['title'] = self.extract(response, 'img.Avatar::attr(src)').extract()[0].encode('utf-8')
        # print item['title']
        # yield item
        # item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        # item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        # yield item
        
        item= {
            'id': self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.profile-navbar.clearfix > a.item.home.first.active::attr(href)'),
            'name': self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div.top > div.title-section.ellipsis > span.name::text'),
            'avatar': self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div.body.clearfix > img::attr(src)'),
            'bio': self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div.top > div.title-section.ellipsis > span.bio::text'),
            'gender': self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div.body.clearfix > div > div > div.items > div:nth-child(1) > span.info-wrap > span > i::attr(class)'),
            'agree': self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-operation.zg-clear > div.zm-profile-header-info-list > span.zm-profile-header-user-agree > strong::text'),
            'thanks': self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-operation.zg-clear > div.zm-profile-header-info-list > span.zm-profile-header-user-thanks > strong::text'),
            'asks': self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.profile-navbar.clearfix > a:nth-child(2) > span::text'),
            'answers': self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.profile-navbar.clearfix > a:nth-child(3) > span::text'),
            'posts': self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.profile-navbar.clearfix > a:nth-child(4) > span::text'),
            'collections': self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.profile-navbar.clearfix > a:nth-child(5) > span::text'),
            'logs': self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.profile-navbar.clearfix > a:nth-child(6) > span::text'),
            'followers': self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-sidebar > div.zm-profile-side-following.zg-clear > a:nth-child(2) > strong::text'),
            'followees': self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-sidebar > div.zm-profile-side-following.zg-clear > a:nth-child(1) > strong::text'),
        }
        item = self.format(item)
        yield item
        headers={
        'Cookie': '_za=44adbaf5-d84b-4642-9ed7-f9ea277e7d45; cap_id="Zjc4NDdjODA0YTViNGIzZDk3ODNjZTE1MjQyZDgzNDk=|1457412486|b84781fc6ceaec9da3c5167f657e8945e39f2ece"; z_c0="QUFCQUZya1lBQUFYQUFBQVlRSlZUWkRtQlZmQ09WVmJSemtkWU50dlpzTVVDSkRvRWltQjRRPT0=|1457412496|d69dded4732afbda4d7be5045ba9761b21d2f3cb"; udid="AGBAvxk3lQmPTiEWuCKqzZj2d1eGXwVa97A=|1457503823"; d_c0="AJDA4kYkogmPTqjcdrH55c1UiT-ehjAaCj4=|1458279968"; q_c1=9137111e22384722bec3bb1a7fc74b88|1458484741000|1429880911000; _xsrf=1177029a662946153628dd613bbb4a89; _ga=GA1.2.2049539814.1432119670; __utmt=1; __utma=51854390.2049539814.1432119670.1459489024.1459489024.1; __utmb=51854390.10.10.1459489024; __utmc=51854390; __utmz=51854390.1459489024.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20111017=1^3=entry_date=20111017=1',
        }
        # print response.request.headers
        # pprint(self.settings['DEFAULT_REQUEST_HEADERS'])
        if len(urlparse(response.url).path.split('/')) == 3:
            yield scrapy.Request(response.url+'/followers', lambda res: self.parse_followers(res, item['followers']))
    def parse_followers(self, response, followers):
        # parse relationship
        xsrf=self.extract(response, 'body > input[type="hidden"]::attr(value)')
        params=self.extract(response, '#zh-profile-follows-list > div::attr(data-init)')
        if not params:
            return
        params=json.loads(params)['params']
        data={
            'params': json.dumps(params, separators=(',', ':')),
            'method': 'next',
            '_xsrf': xsrf
        }
        url='https://www.zhihu.com/node/ProfileFollowersListV2'
        headers= {'Content-Type': 'application/x-www-form-urlencoded'}
        for i in range(followers/20 + 1):
            qs=urllib.urlencode(data)
            yield scrapy.Request(url, method='POST', headers=headers, body=urllib.urlencode(data), callback=self.parse_followers_list)
    def parse_followers_list(self, response):
        # request=response.request
        peoples = json.loads(response.body)
        reg = re.compile(' href="/people/([^/]*?)"')
        for p in peoples['msg']:
            id = reg.search(p).groups()[0]
            # save following
            print id
        # print response.body
    def format(self, item):
        if 'female' in item['gender']:
            item['gender'] = 'female'
        elif 'male' in item['gender']:
            item['gender'] = 'male'
        else: 
            item['gender'] = ''

        item['id'] = item['id'][8:]
        int_fields=('followees', 'followers', 'posts', 'logs', 'asks', 'answers', 'collections', 'agree', 'thanks')
        for f in int_fields:
            item[f] = int(item[f])
        return item
    def extract(self, res, selector):
        return (res.css(selector).extract_first() or u'').encode('utf-8').strip()
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
import pymongo

class People(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    avatar = scrapy.Field()
    bio = scrapy.Field()
    gender = scrapy.Field()
    agree = scrapy.Field(serializer=int)
    thanks = scrapy.Field(serializer=int)
    asks = scrapy.Field(serializer=int)
    answers = scrapy.Field(serializer=int)
    posts = scrapy.Field(serializer=int)
    collections = scrapy.Field(serializer=int)
    logs = scrapy.Field(serializer=int)
    followers = scrapy.Field(serializer=int)
    followees = scrapy.Field(serializer=int)

class Following(scrapy.Item):
    follower = scrapy.Field()
    followee = scrapy.Field()

# class PeopleSpider(CrawlSpider):
class PeopleSpider(scrapy.Spider):
    name = 'people'
    allowed_domains = ['www.zhihu.com']
    handle_httpstatus_list = [403]

    start_urls = [
    'https://www.zhihu.com/explore',
    'https://www.zhihu.com/topics',
    # 'https://www.zhihu.com/people/zhi-shi-jiu-shi-li-liang-13',
    ]

    rules = (
        Rule(LinkExtractor(allow=('zhihu\.com/question/', 'zhihu\.com/topic/'))),

        Rule(LinkExtractor(allow=('zhihu\.com/people/')), callback='parse_item'),
    )

    def start_requests(self):
        client = pymongo.MongoClient('mongodb://localhost:8100')
        people = client['zhihu']['people']
        following = client['zhihu']['following']
        ps=100000
        print following.count()
        # return 
        for i in range(following.count()/ps+1):
            count = 0
            res = following.aggregate([{'$skip': i*ps}, {'$limit':ps}, {'$group':{'_id':'$follower'}}])
            for p in res:
                if people.find_one({'id':p['_id']}) is not None:
                    # print 'duplicate id',p['_id']
                    count +=1
                    continue
                # yield []
                url='https://www.zhihu.com/people/'
                yield scrapy.Request(url+p['_id'], callback=self.parse_item)
            print 'duplicate count:',count
        # yield {}
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
        
        item= People()
        item['id'] = self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.profile-navbar.clearfix > a.item.home.first.active::attr(href)')
        item['name'] = self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div.top > div.title-section.ellipsis > span.name::text')
        item['avatar'] = self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div.body.clearfix > img::attr(src)')
        item['bio'] = self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div.top > div.title-section.ellipsis > span.bio::text')
        item['gender'] = self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div.body.clearfix > div > div > div.items > div:nth-child(1) > span.info-wrap > span > i::attr(class)')
        item['agree'] = self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-operation.zg-clear > div.zm-profile-header-info-list > span.zm-profile-header-user-agree > strong::text')
        item['thanks'] = self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-operation.zg-clear > div.zm-profile-header-info-list > span.zm-profile-header-user-thanks > strong::text')
        item['asks'] = self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.profile-navbar.clearfix > a:nth-child(2) > span::text')
        item['answers'] = self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.profile-navbar.clearfix > a:nth-child(3) > span::text')
        item['posts'] = self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.profile-navbar.clearfix > a:nth-child(4) > span::text')
        item['collections'] = self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.profile-navbar.clearfix > a:nth-child(5) > span::text')
        item['logs'] = self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.profile-navbar.clearfix > a:nth-child(6) > span::text')
        item['followers'] = self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-sidebar > div.zm-profile-side-following.zg-clear > a:nth-child(2) > strong::text')
        item['followees'] = self.extract(response, 'body > div.zg-wrap.zu-main.clearfix > div.zu-main-sidebar > div.zm-profile-side-following.zg-clear > a:nth-child(1) > strong::text')

        item = self.format(item)
        yield item

        if len(urlparse(response.url).path.split('/')) == 3:
            yield scrapy.Request(response.url+'/followers', lambda res: self.parse_followers(res, item['followers'], item['id']))
    def parse_followers(self, response, followers, followee):
        # parse relationship
        xsrf=self.extract(response, 'body > input[type="hidden"]::attr(value)')
        params=self.extract(response, '#zh-profile-follows-list > div::attr(data-init)')
        if not params:
            return
        params=json.loads(params)['params']
        url='https://www.zhihu.com/node/ProfileFollowersListV2'
        headers= {'Content-Type': 'application/x-www-form-urlencoded'}
        data={
            'method': 'next',
            '_xsrf': xsrf
        }
        for i in range(int(followers)/20 + 1):
            cur_params = dict(params)
            cur_params['offset'] = i * 20
            data['params']=json.dumps(cur_params, separators=(',', ':'))
            qs=urllib.urlencode(data)
            yield scrapy.Request(url, method='POST', headers=headers, body=urllib.urlencode(data), callback=lambda res: self.parse_followers_list(res,followee))
    def parse_followers_list(self, response, followee):
        # request=response.request
        peoples = json.loads(response.body)
        reg = re.compile(' href="/people/([^/]*?)"')
        for p in peoples['msg']:
            follower = reg.search(p).groups()[0].encode('utf-8')
            # save following
            following = Following()
            following['followee'] = followee
            following['follower'] = follower
            yield  following
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
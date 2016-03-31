# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class PeopleSpider(CrawlSpider):
    name = 'people'
    allowed_domains = ['www.zhihu.com']
    start_urls = [
    'https://www.zhihu.com/explore',
    'https://www.zhihu.com/topics',
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
# -*- coding: utf-8 -*-
import scrapy


class OwSpider(scrapy.Spider):
    name = 'ow'
    start_urls = ['https://www.huya.com/g/overwatch/']

    def parse(self, response):
        item = []
        rank = 0
        for value in response.css('li.game-live-item'):
            viewers = value.css('i.js-num::text').extract_first()
            if '.' in viewers:
                item.append((
                    int(float(viewers.replace('万', '')) * 10000),
                    value.css('i.nick::text').extract_first()
                ))
            else:
                item.append((
                    int(viewers),
                    value.css('i.nick::text').extract_first()
                ))
        result = sorted(item, reverse=True)
        for i in result:
            rank +=1
            print('rank %s: %s %s人' % (rank, i[1], i[0])) 

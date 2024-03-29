# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    rate = scrapy.Field()
    director = scrapy.Field()


class DirectorItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    agent = scrapy.Field()
    constellation = scrapy.Field()
    films = scrapy.Field()

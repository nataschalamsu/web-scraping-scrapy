# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MangascrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    author = scrapy.Field()
    genre = scrapy.Field()
    viewed = scrapy.Field()
    rating = scrapy.Field()
    link = scrapy.Field()

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from itemloaders.processors import MapCompose, TakeFirst
import scrapy
from w3lib.html import remove_tags


class AmazonscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    img_link = scrapy.Field()
    pass

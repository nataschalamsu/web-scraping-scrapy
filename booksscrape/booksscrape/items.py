# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def remove_unused_class(value):
    return value.replace('star-rating ', '')

def remove_new_line(value):
    return value.replace('\n', '')

def strip_value(value):
    return value.strip()

class BooksscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    rating = scrapy.Field(input_processor = MapCompose(remove_tags, remove_unused_class), output_processor = TakeFirst())
    availability = scrapy.Field(input_processor = MapCompose(remove_tags, remove_new_line, strip_value), output_processor = TakeFirst())
    pass

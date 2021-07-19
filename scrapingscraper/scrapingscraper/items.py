# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def remove_new_line(value):
    return value.replace('\n', '').strip()

def remove_currency(value):
    return value.replace('Rp', '').replace(',00', '').strip()
class ScrapingscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor = MapCompose(remove_tags, remove_new_line), output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_tags, remove_new_line, remove_currency), output_processor = TakeFirst())

import scrapy
from scrapy.loader import ItemLoader
from booksscrape.items import BooksscrapeItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    # allowed_domains = ['https://books.toscrape.com']
    start_urls = ['https://books.toscrape.com/index.html']

    def parse(self, response):
        for books in response.xpath('//article[@class="product_pod"]'):
            item = ItemLoader(item = BooksscrapeItem(), selector=books)

            item.add_css('name', 'h3 a::attr(title)')
            item.add_css('price', 'p.price_color')
            item.add_css('rating', 'p.star-rating::attr(class)')
            item.add_css('availability', 'p.instock.availability')

            yield item.load_item()

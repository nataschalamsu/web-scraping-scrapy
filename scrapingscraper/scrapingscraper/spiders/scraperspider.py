import scrapy
from scrapy.loader import ItemLoader
from scrapingscraper.items import ScrapingscraperItem


class ScraperspiderSpider(scrapy.Spider):
    name = 'scraperspider'
    start_urls = ['https://walltswallet.com/collections/bifold-wallet?sort_by=best-selling']

    def parse(self, response):
        for products in response.xpath('//div[@class="productitem--info"]'):
            l = ItemLoader(item = ScrapingscraperItem(), selector=products)

            l.add_css('name', 'h2.productitem--title > a:nth-child(n+1)::text')
            l.add_css('price', 'span.money::text')

            yield l.load_item()

        next_page = response.xpath('//li[@class="pagination__next"]/a/@href').extract()[0]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

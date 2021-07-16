import scrapy
from scrapingscraper.items import ScrapingscraperItem


class ScraperspiderSpider(scrapy.Spider):
    name = 'scraperspider'
    start_urls = ['https://walltswallet.com/collections/bifold-wallet?sort_by=best-selling']

    def parse(self, response):
        name = response.xpath('//h2[@class="productitem--title"]/a/text()').extract()
        price = response.xpath('//div[@class="price--main"]/span/text()').extract()

        for product in zip(name, price):
            scraped_data = {
                'Name': product[0].strip(),
                'Price': product[1].strip(),
            }

            yield scraped_data

        next_page = response.xpath('//li[@class="pagination__next"]/a/@href').extract()[0]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

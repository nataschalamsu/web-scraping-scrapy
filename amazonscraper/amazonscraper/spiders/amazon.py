import scrapy
from scrapy.loader import ItemLoader
from amazonscraper.items import AmazonscraperItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1626838219&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0']
    start_urls = ['https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1626838219&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0']

    def parse(self, response):
        for books in response.xpath('//div[@class="a-section a-spacing-none"]'):
            items = ItemLoader(item = AmazonscraperItem(), selector=books)

            items.add_xpath('name', '//span[@class="a-size-medium a-color-base a-text-normal"]/text()')
            items.add_xpath('//a[@class="a-size-base a-link-normal"]/text()')
            items.add_xpath('//span[@class="a-offscreen"]/text()')
            items.add_xpath('//img[@class="s-image"]/@src')

            yield items.load_item()
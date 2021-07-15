import scrapy
from mangascrapy.items import MangascrapyItem


class MangaspiderSpider(scrapy.Spider):
    name = 'mangaspider'
    # allowed_domains = ['https://manganato.com/']
    start_urls = ['https://manganato.com/genre-all/']

    for i in range(2,100):
        start_urls.append(f'https://manganato.com/genre-all/{i}')

    def parse(self, response):
        for href in response.css('a.genres-item-name.text-nowrap.a-h::attr(href)'):
            url = href.extract()
            
            yield scrapy.Request(url, callback=self.parse_dir_contents)


    def parse_dir_contents(self, response):
        item = MangascrapyItem()

        item['name'] = response.xpath('//div[@class="story-info-right"]/h1/text()').extract()
        item['author'] = response.xpath('//td[@class="table-value"]/a/text()').extract()[0]
        item['genre'] = response.xpath('//td[@class="table-value"]/a/text()').extract()[1:]
        item['viewed'] = response.xpath('//span[@class="stre-value"]/text()').extract()[1]
        item['rating'] = response.xpath('//em[@property="v:average"]/text()').extract()
        item['link'] = response.xpath('//div[@class="panel-story-info-description"]/text()').extract()[1].strip()

        yield item
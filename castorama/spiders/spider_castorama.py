import scrapy
from scrapy.http import HtmlResponse
from items import CastoramaItem
from scrapy.loader import ItemLoader

class SpiderCastoramaSpider(scrapy.Spider):
    name = "spider_castorama"
    allowed_domains = ["castorama.ru"]
    start_urls = ["https://castorama.ru"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.page = 1
        self.start_urls = [f"https://www.castorama.ru/catalogsearch/result/?q={kwargs.get('query')}&PAGEN_3={self.page}"]

    def parse(self, response: HtmlResponse):
        links = response.xpath('//a[@class="product-card__img-link"]')
        if links:
            for link in links:
                yield response.follow(link, callback=self.parse_item)

    def parse_item(self, response:HtmlResponse):
        loader = ItemLoader(item=CastoramaItem(), response=response)
        loader.add_xpath('name', '//h1/text()')
        loader.add_xpath('price', "//span[@class='price']//text()")
        loader.add_xpath('photos', "//li[contains(@class, 'top-slide swiper-slide')]//img/@src")
        loader.add_value('url', response.url)
        yield loader.load_item()
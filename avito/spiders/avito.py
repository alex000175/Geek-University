import scrapy
from scrapy_splash import SplashRequest
from scrapy.http import HtmlResponse
from items import AvitoparserItem
from scrapy.loader import ItemLoader

class AvitoSpider(scrapy.Spider):
    name = "avito"
    allowed_domains = ["avito.ru"]
    start_urls = ["https://avito.ru"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.page = 1
        self.start_urls = [f"https://www.avito.ru/rostov-na-donu?p={self.page}&q={kwargs.get('query')}"]

    def start_requests(self):
        if not self.start_urls and hasattr(self, "start_url"):
            raise AttributeError(
                "Crawling could not start: 'start_urls' not found "
                "or empty (but found 'start_url' attribute instead, "
                "did you miss an 's'?)"
            )
        for url in self.start_urls:
            yield SplashRequest(url)

    def parse(self, response: HtmlResponse):
        links = response.xpath('//a[@data-marker="item-title"]')
        if links:
            for link in links:
                # yield response.follow(link, callback=self.parse_ads)
                yield SplashRequest('https://avito.ru' + str(link), callback=self.parse_ads)

    def parse_ads(self, response:HtmlResponse):
        # pass
        loader = ItemLoader(item=AvitoparserItem(), response=response)
        loader.add_xpath('name', '//h1/text()')
        loader.add_xpath('info', "//div[@class='style-item-description-text-mc3G6']/text()")
        loader.add_xpath('price', "//span[@class='style-price-value-string-rWMtx']/text()")
        loader.add_xpath('photos', "//span[@class = 'image-frame-cover-lQG1h]/img/@src")
        loader.add_value('url', response.url)
        yield loader.load_item()
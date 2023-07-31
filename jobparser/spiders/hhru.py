import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem


class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    start_urls = ["https://rostov.hh.ru/search/vacancy?area=1&search_field=name&search_field=company_name&search_field=description&enable_snippets=false&text=python",
                  "https://rostov.hh.ru/search/vacancy?area=2&search_field=name&search_field=company_name&search_field=description&enable_snippets=false&text=python"
                  ]

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse) 

        links = response.xpath("//a[@class='serp-item__title']/@href").getall()

        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)


    def vacancy_parse(self, response: HtmlResponse):
        name = response.xpath("//h1/text()").get()
        salary = response.xpath("//div[@data-qa='vacancy-salary']/span//text()").getall()
        url = response.url
        company = response.xpath("//a[@data-qa='vacancy-company-name']//text()").get()
        city = response.xpath("//p[@data-qa='vacancy-view-location']//text()").get()
        yield JobparserItem(name=name, salary=salary, url=url, company=company, city=city)


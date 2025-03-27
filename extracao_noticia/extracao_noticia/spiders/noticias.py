import scrapy
from scrapy.http import Response


class NoticiasG1Spider(scrapy.Spider):
    name = "noticias"
    allowed_domains = ["exemplo.com"]
    start_urls = ["https://exemplo.com"]

    def parse(self, response: Response):
        pass


class NoticiasG1Spider(scrapy.Spider):
    pass

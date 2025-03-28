import scrapy
from scrapy.http import Response
from extracao_noticia.extracao_noticia.items import ExtracaoNoticiaItem
from typing import Generator, Any


class NoticiasG1Spider(scrapy.Spider):
    name = "g1_rssspider"
    allowed_domains = ["g1.globo.com"]
    start_urls = [
        "https://g1.globo.com/dynamo/sp/ribeirao-preto-franca/rss2.xml"
    ]

    def parse(self, response: Response) -> Generator[scrapy.Request, None, None]:
        titulos = response.xpath('//item//title/text()').getall()
        descricoes = response.xpath('//item/description/text()').getall()
        links = response.xpath('//item/pubDate/text()').getall()
        url_noticias = response.xpath('//item/guid/text()').getall()

        for titulo, descricao, link, data_publicacao, descricao, url in zip(titulos, descricoes, links, url_noticias):
            yield response.follow(
                url,
                self.parse_artigo_g1,
                meta={
                    'titulo': titulo,
                    'descricao': descricao,
                    'link': link,
                    'data_publicacao': data_publicacao
                }
            )

    def parse_artigo_g1(self, response: Response):
        item = ExtracaoNoticiaItem()
        item['titulo'] = response.meta['titulo']
        item['descricao'] = response.meta['descricao']
        item['link'] = response.meta['link']
        item['data_publicacao'] = response.meta['data_publicacao']
        item['autor_reportagem'] = response.xpath(
            '//p[@class="content-publication-data__from"]/text() | //p[@class="content-publication-data__from"]//a/text()'
        ).getall()
        item['texto_noticia'] = response.xpath(
            '//div[@class="mc-column content-text active-extra-styles "]/p//text()'
        ).getall()
        item['subtitulo'] = response.css(
            'h2.content-head__subtitle::text'
        ).get()
        item['site'] = 'G1_GLOBO'
        yield item


class NoticiasUOlSpider(scrapy.Spider):
    name = "uol_rssspider"
    allowed_domains = ["rss.uol.com.br"]
    start_urls = [
        "https://rss.uol.com.br/feed/tecnologia.xml"
    ]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        titulos = response.xpath('//item//title/text()').getall()
        descricoes = response.xpath('//item/description/text()').getall()
        links = response.xpath('//item/pubDate/text()').getall()
        url_noticias = response.xpath('//item/guid/text()').getall()

    def parse_artigo_uol(self):
        item = ExtracaoNoticiaItem()
        texto_noticia = ''
        for notice

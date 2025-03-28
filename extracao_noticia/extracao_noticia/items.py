# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from typing import List


class ExtracaoNoticiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = scrapy.Field(serialize=str)
    descricao = scrapy.Field(serialize=str)
    link = scrapy.Field(serialize=str)
    data_publicacao = scrapy.Field(serialize=str)
    autor_reportagem = scrapy.Field(serialize=List[str])
    texto_noticia = scrapy.Field(serialize=List[str])
    subtitulo = scrapy.Field(serialize=str)
    site = scrapy.Field(serialize=str)

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader

from scrapy.loader.processors import TakeFirst, MapCompose

def remove_dollar_sign(value: str):
    return value.replace("$", "")


class ProductScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_url = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_dollar_sign),
                         output_processor=TakeFirst())
    title = scrapy.Field(output_processor=TakeFirst())
    img_url = scrapy.Field(output_processor=TakeFirst())

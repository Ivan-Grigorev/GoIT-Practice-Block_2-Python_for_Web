import itemloaders
import scrapy
from scrapy.loader import ItemLoader

from product_scrapper.items import ProductScrapperItem


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['clever-lichterman-044f16.netlify.app']
    start_urls = ['https://clever-lichterman-044f16.netlify.app/products/taba-cream.1/']

    def parse(self, response):
        # item = ProductScrapperItem()
        
        # item["product_url"] = response.url
        # item["price"] = response.xpath("//div[@class='my-4']/span/text()").get()
        # item["title"] = response.xpath("//h4[@class='font-weight-medium']/text()").get() 
        # item["img_url"] = response.xpath("//div[@class='product-slider']//img/@src").get(0)

        # return item
        l = ItemLoader(item=ProductScrapperItem(), response=response)
        l.add_value('product_url', response.url)
        l.add_xpath('price', "//div[@class='my-4']/span/text()")
        l.add_xpath('title', "//h4[@class='font-weight-medium']/text()")
        l.add_xpath('img_url', "//div[@class='product-slider']//img/@src")

        return l.load_item()

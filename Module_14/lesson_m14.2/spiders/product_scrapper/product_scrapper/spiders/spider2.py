import scrapy
from scrapy.loader import ItemLoader
from product_scrapper.items import ProductScrapperItem
from scrapy.spiders import SitemapSpider


class Spider2Spider(SitemapSpider):
    name = 'spider2'

    sitemap_urls = ['https://clever-lichterman-044f16.netlify.app/sitemap.xml']
    sitemap_rules = [
        ('/products/*', 'parse')
    ]

    # allowed_domains = ['domain.com']
    # start_urls = ['http://domain.com/']

    def parse(self, response):
        l = ItemLoader(item=ProductScrapperItem(), response=response)
        l.add_value('product_url', response.url)
        l.add_xpath('price', "//div[@class='my-4']/span/text()")
        l.add_xpath('title', "//h4[@class='font-weight-medium']/text()")
        l.add_xpath('img_url', "//div[@class='product-slider']//img/@src")

        return l.load_item()


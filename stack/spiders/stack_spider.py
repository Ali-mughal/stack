#https://realpython.com/web-scraping-with-scrapy-and-mongodb/
from scrapy import Spider
from stack.items import StackItem

class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ["http://stackoverflow.com/questions?pagesize=50&sort=newest"]
    def parse(self, response):
        title=response.css('div.summary >h3>a::text').getall()
        urls=response.css('div.summary >h3>a::attr(href)').getall()
        for title,url in zip(title,urls):
            item = StackItem()
            item['title'] = title
            item['url'] = url
            yield item


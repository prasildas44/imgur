import scrapy

from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.contrib.linkextractors import LinkExtractor
from imgur.items import ImgurItem


class ImgurSpider(CrawlSpider):

	name = 'imgur'
	allowed_domains = ['imgur.com']
	start_urls = ['http://www.imgur.com/r/weed']

	rules = [
		Rule(LinkExtractor(allow=['/.*']), "parse_imgur") 

	]


	def parse_imgur(self, response):

		image=ImgurItem()

		image['title'] = response.xpath("//h1/text()").extract()

		rel = response.xpath("//img/@src")[0].extract()

		image['image_urls'] = ['http:' + rel]

		return image





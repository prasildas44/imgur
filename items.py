import scrapy

class ImgurItem(scrapy.Item):
	title = scrapy.Field()
	image_urls = scrapy.Field()
	# images = scrapy.Field()

BOT_NAME = 'imgur'

SPIDER_MODULES = ['imgur.spiders']
NEWSPIDER_MODULE = 'imgur.spiders'
ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline':1}
IMAGES_STORE = '/home/prasil/Desktop/das'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'imgur (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

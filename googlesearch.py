from bs4 import BeautifulSoup
import scrapy
import logging
from furl import furl
from scrapy.http import FormRequest
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import Spider

class PartnersSpider(Spider):
	name = 'googlespider'
	start_urls = ['https://www.google.fr/search?q=test&oq=test&aqs=chrome..69i57j69i61j0l4.615j0j4&sourceid=chrome&ie=UTF-8']
	end = 0

	def __init__(self):
		logging.getLogger('scrapy').setLevel(logging.WARNING)

	"""def parseLink(self, response):
		print("\n======================================\n")
		if end == 0:
			googlelinks = response.xpath('//h3/a/@href').extract()
			for index, link in enumerate(googlelinks):
				f = furl(link)
				googlelinks[index] = f.args['q']
		else:
			googlelinks = response.css('li.next a::attr("href")').extract()
		end += 1;
		for link in googlelinks:
			print(link)
		return (googlelinks)"""

	def parse(self, response):
		googlelinks = response.xpath('//h3/a/@href').extract()
		if self.end == 0:
			for index, link in enumerate(googlelinks):
				f = furl(link)
				googlelinks[index] = f.args['q']
		self.end += 1;
		requests = []
		for link in googlelinks:
			print (link)
			yield scrapy.Request(link, callback=self.parse)
		#return (requests)

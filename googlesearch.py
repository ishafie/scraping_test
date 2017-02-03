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
	is_google_search = true
	urls_set = set()

	def __init__(self):
		logging.getLogger('scrapy').setLevel(logging.WARNING)

	def parse(self, response):
		if "text/html" not in response.headers.getlist("Content-Type"):
			yield None
		if self.is_google_search == true:
			googlelinks = parseGoogleLink(response.xpath('//h3/a/@href').extract())
		else :
			googlelinks = response.xpath('//a/@href').extract()
		self.is_google_search = false;
		requests = []
		cdt_filter = lambda x: x and not "wiki" in x and not x.startswith('#')
		addPathToGoogleLink.url = response.url
		for link in map(addPathToGoogleLink, filter(cdt_filter, googlelinks)):
			print(link)
			if link in self.urls_set:
				yield None
			else :
				self.urls_set.add(link)
				print(link)
				yield scrapy.Request(link, callback=self.parse)

def addPathToGoogleLink(link):
	if not link.startswith('http'):
		if not link.startswith('/') :
			link = '/'.join(addPathToGoogleLink.url.split('/')[:3]) + '/' + link
		else :
			link = '/'.join(addPathToGoogleLink.url.split('/')[:3]) + link
	return (link)

def parseGoogleLink(googlelinks):
	for index, link in enumerate(googlelinks):
		f = furl(link)
		googlelinks[index] = f.args['q']
	return googlelinks

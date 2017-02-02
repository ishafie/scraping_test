from bs4 import BeautifulSoup
import scrapy
import logging

class PartnersSpider(scrapy.Spider):
	name = 'partnerspider'
	start_urls = ['https://raw.githubusercontent.com/ishafie/image_compression_quadtrees/master/README.md']

	def __init__(self):
		logging.getLogger('scrapy').setLevel(logging.WARNING)

	def parse(self, response):
		print("\n======================================\n")

		soup = BeautifulSoup(response.body, 'html.parser')
		print(soup.prettify())



		next_page = response.css('li.next a::attr("href")').extract_first()
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse)
		print("\n=====================================\n")

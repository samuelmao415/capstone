
from scrapy import Spider, Request
from nordstrom.items import NordstromItem

class NordstromSpider(Spider):
	name = "nordstrom_spider"
	allowed_urls = ['https://shop.nordstrom.com/']
	start_urls = ['https://shop.nordstrom.com/c/womens-tops-tees?breadcrumb=Home%2FWomen%2FClothing%2FTops&top=72&offset=0&page=1&sort=Boosted']

	def parse(self,response):
		allurls = ['https://shop.nordstrom.com/c/womens-tops-tees?breadcrumb=Home%2FWomen%2FClothing%2FTops&top=72&offset=0&page={}&sort=Boosted'.format(x) for x in range(1,6)]
		for r in allurls: 
			images = response.xpath('//img[@name="product-module-image"]/@src').extract()
			#yield Request(url = r, callback = self.parse_all_urls)

	#def parse_all_urls(self,response):
		#urls = response.xpath('//h3/a[@class="linkWrapper_Z1Y4dTj"]/@href').extract()  
		#newurls = map(lambda x:"https://shop.nordstrom.com" + x,urls)

		#for url in newurls:
			#yield Request(url=url, callback = self.parse_result_page)

	#def parse_result_page(self,response):
		#name = response.xpath('//h1[@class="dark_1uNQRe brandon_Z1xXd4V small_Tz6h1 YMqEq"]/text()').extract()
		#price = response.xpath('//span[@class="currentPriceString_16T2V5"]/text()').extract()
		#description = response.xpath('//div[@data-element="selling-statement"]/text()').extract()
		

		item = NordstromItem()
		#item['name'] = name
		#item['price'] = price
		#item['description'] = description
		item['images'] = images

		yield item 

	
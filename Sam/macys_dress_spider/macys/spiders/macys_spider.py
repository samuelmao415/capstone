from scrapy import Spider,Request
from macys.items import MacysItem
#import urllib.request


class macys(Spider):
    name="macys_spider"
    allowed_urls=["https://www.macys.com/shop/womens-clothing"]
    start_urls=["https://www.macys.com/shop/womens-clothing/dresses?id=5449"]
    def parse(self,response):
        result_urls=['https://www.macys.com/shop/womens-clothing/dresses/Pageindex/{}?id=5449'.format(x) for x in range(1,130)]
        for url in result_urls:
            yield Request(url=url, callback=self.parse_clothing_page)
        print("parse"*20)


    def parse_clothing_page(self,response):
        #extract product link from the first pages
        macyurl="https://www.macys.com"
        #list comprehension to concat domain with sublinks
        product = response.xpath('//div[@class="productDescription"]/a/@href').extract()
        # response.xpath('//span[@class="regular"]').extract()
        # response.xpath('normalize-space(//span[@class="regular"])').extract()
        # ' '.join(s.strip() for s in response.xpath('//span[@class="regular"]')).extract()
        res=[macyurl+s for s in product]
        for url in res:
            yield Request(url=url, callback=self.parse_item_page)
        print("parse_clothing_page"*20)
#image
# -name
# -product description (all of it)
# -price
# -material description (if any)

    def parse_item_page(self,response):
        #name=response.xpath('.//h1[@itemprop="name"]').extract()
        item=MacysItem()
        # main_image=response.xpath('//li[@class="main-image swiper-slide"]/img/@src').extract()
        # other_images=response.xpath('//li[@class="main-image swiper-slide"]/img/@data-src').extract()
        # #except the main image, the page usually comes with two more images
        # try:
        #     other_image_1=other_images[0]
        #     other_image_2=other_images[1]
        #     item["other_image_1"]=other_image_1
        #     item["other_image_2"]=other_image_2
        # except:
        #     pass
        # prodcut_description=response.xpath('//p[@class="reset-font c-margin-1v"]/text()').extract()
        # material_description=response.xpath('//ul[@data-auto="product-description-bullets"]/li/text()').extract()
        price=response.xpath('//div[@data-auto="main-price"]/text()').extract_first()
        product_name=response.xpath('//h1[@data-auto="product-name"][@itemprop="name"]/text()').extract_first().strip()
        #download image
        # full_file_name=list("./pics/sm{}.tif".format(x) for x in range(1,100))
        # urllib.request.urlretrieve(main_image,full_file_name)


        #
        # item["main_image"]=main_image
        #
        # item["prodcut_description"]=prodcut_description
        # item["material_description"]=material_description
        item["price"]=price
        item["product_name"]=product_name

        yield item
        print("item"*20)

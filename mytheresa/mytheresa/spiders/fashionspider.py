from tkinter import Y
import scrapy

class MytheresaSpider(scrapy.Spider):
	name 	= 'mytheresa'
	starter_url	= ['https://www.mytheresa.com/int_en/men/shoes.html']

	def parse(self,response):
		for products in response.css('li.item'):
			yield {
				'image_url'	: products.css('a.product-image img::attr(data-src)').get(),
				'brand'		: products.css('span.ph1::text').get(),
				'product_name': products.css('a.pa1-rm::text').get(),


			}
import scrapy


class NepaldriveSpider(scrapy.Spider):
    name = "nepaldrive"
    allowed_domains = ["www.nepaldrive.com"]
    start_urls = ["https://www.nepaldrive.com/popular-car"]

    def parse(self, response):
        # get all the card link
        links = response.css('div.product-inner a.pro-view::attr(href)').getall()
        yield from response.follow_all(links, self.detail_page)

    def detail_page(self, response):
        data = {}
        title = response.css('h1::text').get()
        url = response.url
        dta = {
            'title': title,
            'url': url
        }
        for item in response.css('ul.info-features li'):
            key = item.css('b::text').get()
            if key == "Brand":
                data['brand'] = item.css('a::text').get()
            elif key == "Power":
                data['power'] = item.css('::text').getall()[1]
            elif key == "Fuel":
                data['power'] = item.css('::text').getall()[1]
            elif key == "Engine":
                data['engine'] = item.css('::text').getall()[1]

        for item in response.css('ul.scrollmenu li'):
            key = item.css('strong::text').get()
            value = item.css('p::text').get()
            if key == "Wheel Size":
                data['wheel_size'] = value
            elif key == "TyreType":
                data['type_type'] = value
            elif key == "Transmission":
                data['transmission'] = value
            elif key == "Seating Capacity":
                data['seating capacity'] = value
            elif key == "Fuel Tank":
                data['fuel_tank'] = value
            elif key == "Cylinders":
                data['cylinders'] = value
        
        for item in response.css('section#sectionSpecifications table tbody tr'):
            key = item.css('strong::text').get()
            if key != None:
                key = key.lower()
                data[key] = item.css('td::text').get()
            else:
                continue
        yield data
                


        

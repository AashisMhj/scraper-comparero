import scrapy


class Ktm2daySpider(scrapy.Spider):
    name = "ktm2day"
    allowed_domains = ["www.ktm2day.com", "ktm2day.com"]
    start_urls = "https://www.ktm2day.com/2013/03/10/bikes-in-nepal/"

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls, callback=self.parse)

    def parse(self, response):
        links = response.css('table#tablepress-143 td.column-1 a::attr(href)').getall()
        yield from response.follow_all(links, self.listing_page)

    def listing_page(self, response):
        posts =response.css('table.tablepress tbody tr.even a::attr(href),table.tablepress tbody tr.odd a::attr(href)').getall()
        yield from response.follow_all(posts, self.parse_detail)

    def parse_detail(self, response):
        title =  response.css('h1.single-post-title span::text').get()
        image = response.css('img::attr(src)').get()
        data = {
            'title': title,
            'url': response.url,
            'image': image
        }
        details = response.css('ul.tab_content li').getall()
        for i in details:
            text = i.css('strong::text').get()
            if text == 'Engine ':
                data['engine'] = i.css('::text').getall()[2]
            elif text == 'Displacement':
                data['displacement'] = i.css('::text').getall()[1]
            elif text == 'Max Net Power':
                data['power'] = i.css('::text').getall()[1]
            elif text == 'Fuel Tank Capacity' :
                data['fuel'] = i.css('::text').getall()[1]
            else :
                pass
        yield data

    def test(response):
        title =  response.css('h1.single-post-title span::text').get()
        image = response.css('img::attr(src)').get()
        data = {
            'title': title,
            'url': response.url,
            'image': image
        }
        # details = response.css('ul.tab_content li')
        # for i in details:
        #     text = i.css('strong::text').get()
        #     print(text)
        #     if text == 'Engine ':
        #         data['engine'] = i.css('::text').getall()[2]
        #     elif text == 'Displacement':
        #         data['displacement'] = i.css('::text').getall()[1]
        #     elif text == 'Max Net Power':
        #         data['power'] = i.css('::text').getall()[1]
        #     elif text == 'Fuel Tank Capacity' :
        #         data['fuel'] = i.css('::text').getall()[1]
        #     else :
        #         pass
        print(data)
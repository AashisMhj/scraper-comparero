import scrapy

class IttiSpider(scrapy.Spider):
    name = "itti"
    allowed_domains = ["itti.com.np"]
    start_urls = ["https://itti.com.np"]

    def parse(self, response):
        # get all the series link from the nav
        links = response.css('li.other-toggle')[0].css('.sm_megamenu_title .sm_megamenu_title a::attr(href)')
        yield from response.follow_all(links, self.listing_page)

    def listing_page(self, response):
        posts = response.css('div.box-image a::attr(href)')
        yield from response.follow_all(posts, self.parse_detail)

        pagination_links = response.css('li.pages-item-next a::attr(href)').get()
        if pagination_links != None:
            yield scrapy.Request(pagination_links)

    def parse_detail(self, response):
        data = {}
        title = response.css('span[itemprop=name]::text').get()
        url = response.url
        data ={
         'title': title,
         'url': url,
        }
        for item in response.css('div.product tr'):
            row = item.css('td::text')
            if len(row) == 0:
                continue
            row = row.get()
            if row == "Brand":
                data['brand'] = item.css('td a::text').get()
            elif row == "Series":
                data['series'] = item.css('td a::text').get()
            elif row == "CPU":
                data['cpu'] = item.css('span::text').get()
            elif row == "Graphics":
                data['graphics'] = item.css('span::text').get()
            elif row == 'Memory':
                data['memory'] = item.css('span::text').get()
            elif row == "Display":
                data['display'] = item.css('span::text').get()
            elif row == "Type":
                result = item.css('td a::text').get()
                if result == None:
                    result = item.css('span::text').get()
                data['type'] = result
            elif row == "Connections":
                result = item.css('div.h5::text').get()
                # data['connection'] = ' '.join(result)
                data['connection'] = result 
            elif row == "Networking":
                data['networking'] = item.css('td a::text').get()
            elif row == "Storage":
                data['storage'] = item.css('td::text')[1].get()
            elif "Size" in row:
                data['size'] = ' '.join(item.css('td span::text').extract())
            elif row == "Battery":
                data['battery'] = item.css('span::text').get()
            elif "Camera" in row:
                pass
            elif row == "Weight":
                pass
        yield data

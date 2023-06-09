import scrapy


class NeostoreSpider(scrapy.Spider):
    name = "neostore"
    allowed_domains = ["neostore.com.np"]
    start_urls = ["https://neostore.com.np/product-category/mobile-brands"]

    def parse(self, response):
        # get all the card link
        links = response.css('div.product-item-box a::attr(href)')
        yield from response.follow_all(links, self.detail_page)

        pagination_link = response.css('a[rel=next]::attr(href)').get()
        if pagination_link != None:
            yield scrapy.Request(pagination_link)

    def detail_page(self, response):
        data = {}
        title = response.css('h1.product_title::text').get(),
        url = response.url,
        data = {
            'title': title,
            'url': url,
        }
        for item in response.css('tbody tr'):
            row = item.css('td')
            if len(row) == 0:
                continue
            table_rows = row.css('td::text').getall()
            header = table_rows[0]
            value = table_rows[1]
            if header == "Category":
                data['category'] = value
            elif header == "Brand":
                data['brand'] = value
            elif 'Display' in header:
                data['display'] = value
            elif 'Battery' in header:
                data['battery'] = value
            elif 'Internal' in header:
                data['internal_storage'] = value
            elif header == 'Primary Camera':
                data['back_camera'] = value
            elif header == 'Secondary Camera':
                data['front_camera'] = value
            elif 'Chipset' in header:
                data['chip'] = value
            elif 'Operating' in header:
                data['os'] = value
            elif header == 'Processor':
                data['processor'] = value
            elif 'Sim' in header:
                data['sim_type'] = value

        yield data
    def __del__(self, reason):
        self.db_handler.close()
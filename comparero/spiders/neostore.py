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
        yield {
            'title': response.css('h1.product_title::text').get(),
            'url': response.url,
            'brand': response.css('span.loop-product-categories a::text').getall()[1],
            'chip': response.css('tbody tr')[9].css('td::text').getall()[1]
        }
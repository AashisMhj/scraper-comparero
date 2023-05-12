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
        yield {
            'title': response.css('span[itemprop=name]::text').get(),
            'url': response.url,
            'brand': response.css('div.product tr')[0].css('td a::text').get(),
            'cpu': response.css('div.product tr')[1].css('td span::text').get(),
            'graphics': response.css('div.product tr')[2].css('td span::text').get()
        }
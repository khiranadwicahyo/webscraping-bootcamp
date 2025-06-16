import scrapy


class WorldometersSpider(scrapy.Spider):
    name = "worldometers"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        # title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a')

        for country in countries:
            country_name = country.xpath('.//text()').get()
            link = country.xpath('.//@href').get()
            


            # untuk menngambil link lengkap ada dua cara

            # 1. Menggunakan response.urljoin
            # absoulute_url = f'https://www.worldometers.info{link}'
            # yield response.urljoin(url=abosolute_url)

            # 2. Menggunakan response.follow
            # yield response.follow(url=link) # cukup gunakan link relatif

            # untuk mengembalikan data dalam bentuk dictionary
            # yield {
            #     "countries": country_name,
            #     "links": link,
            # }

            yield response.follow(url=link, callback=self.parse_country, meta={"country": country_name})

    def parse_country(self, response):
        # untuk mengambil data dari halaman negara
        rows = response.xpath('(//table[contains(@class, "table")])[1]//tbody/tr')

        country = response.request.meta['country']
        for row in rows:
            year = row.xpath('.//td[1]/text()').get()
            population = row.xpath('.//td[2]/text()').get()

            yield {
                "country": country,
                "year": year,
                "population": population,
            }

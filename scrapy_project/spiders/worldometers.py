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
            yearly_change_percentage = row.xpath('.//td[3]/text()').get()
            yearly_change_amount = row.xpath('.//td[4]/text()').get()
            migrants_net = row.xpath('.//td[5]/text()').get()
            median_age = row.xpath('.//td[6]/text()').get()
            fertility_rate = row.xpath('.//td[7]/text()').get()
            density = row.xpath('.//td[8]/text()').get()
            urban_population_percentage = row.xpath('.//td[9]/text()').get()
            urban_population_amount = row.xpath('.//td[10]/text()').get()
            country_share_of_world_population = row.xpath('.//td[11]/text()').get()
            world_population = row.xpath('.//td[12]/text()').get()
            golbal_rank = row.xpath('.//td[13]/text()').get()

            yield {
                "country": country,
                "year": year,
                "population": population,
                "yearly change (%)": yearly_change_percentage,
                "yearly_change_amount": yearly_change_amount,
                "migrants (net)": migrants_net,
                "median_age": median_age,
                "fertility_rate": fertility_rate,
                "density (P/km²)": density,
                "urban pop (%)": urban_population_percentage,
                "urban population": urban_population_amount,
                "country share of world population": country_share_of_world_population,
                "world_population": world_population,
                "global_rank": golbal_rank,
            }

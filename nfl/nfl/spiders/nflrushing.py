import scrapy


class NflrushingSpider(scrapy.Spider):
    name = 'nflrushing'
    allowed_domain = ['pro-football.com']
    start_urls = ['https://www.pro-football-reference.com/years/2021/rushing.htm']


    def parse(self, response):
        for jogadores in response.css("th.right+ .left").css('td'):
            link = response.urljoin(jogadores.css("td").css("a::attr(href)").get())
            print(link)
            yield scrapy.Request(link, callback=self.parse_details)

    def parse_details(self, response):
        nome = response.css("h1 span::text").get()
        time = response.css("strong+ span a::text").get()
        colegio = response.css("p:nth-child(7) strong+ a::text").get()
        jogos_total = response.css(".p1:nth-child(2) .p1:nth-child(1) p::text").get()
        tentativas_rushing = response.css(".p1+ .p1 .p1:nth-child(1) p::text").get()
        td_rushing = response.css(".p2+ .p1 p::text").get()


        yield {
            "Nome": nome,
            "Time": time,
            "Colegio": colegio,
            "Jogos Totais": jogos_total,
            "Tentativas de Rush": tentativas_rushing,
            "Touchdowns com Rush": td_rushing
        }




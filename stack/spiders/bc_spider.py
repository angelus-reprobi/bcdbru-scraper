from scrapy import Spider, Request
from scrapy.selector import Selector

from stack.items import BCItem

class BCSpider(Spider):
    name = "bc"
    allowed_domains = ["db.bordercollie.ru"]

    def start_requests(self):
        for id in range (63160, 63163):
            yield Request('http://db.bordercollie.ru/details.php?id=' + repr(id), self.parse)

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)

        textFields = response.xpath('//div[@class="content"]/table//tr/td[2]/text()')
        regFields = response.xpath('//div[@class="content"]/table//tr/td[3]/table/tr/td/text()')
        linkTextFields = response.xpath('//div[@class="content"]/table//tr/td[2]/a[1]/text()')
        linkHrefFields = response.xpath('//div[@class="content"]/table//tr/td[2]/a[1]/@href')
        imgFields = response.xpath('//div[@class="content"]/table//tr/td[2]/img/@src')

        yield BCItem(
            id = response.url.split('=')[-1],
            regName = textFields[7].extract().strip(),
            breeder = linkTextFields[0].extract().strip(),
            owner = linkTextFields[1].extract().strip(),
            kennel = textFields[10].extract().strip(),
            sire = linkHrefFields[2].extract().strip().split('=')[-1],
            dam = linkHrefFields[3].extract().strip().split('=')[-1],
            callName = textFields[12].extract().strip(),
            sex = textFields[13].extract().strip(),
            dateOfBirth = textFields[14].extract().strip(),
            dateOfDeath = textFields[15].extract().strip(),
            countryOfBirth = textFields[16].extract().strip(),
            countryOfStanding = textFields[17].extract().strip(),
            size = textFields[18].extract().strip(),
            weight = textFields[19].extract().strip(),
            colour = textFields[20].extract().strip(),
            coat = textFields[21].extract().strip(),
            hipScore = textFields[22].extract().strip(),
            elbowScore = textFields[23].extract().strip(),
            distinguishingFeatures = textFields[24].extract().strip(),
            titles = textFields[25].extract().strip(),
            regNo = regFields[1].extract().strip(),
            chipNo = regFields[3].extract().strip(),
            img = imgFields[0].extract(),
        )
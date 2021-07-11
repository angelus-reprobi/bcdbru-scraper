# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class BCItem(Item):
    id = Field()
    regName = Field()
    breeder = Field()
    owner = Field()
    kennel = Field()
    sire = Field()
    dam = Field()
    callName = Field()
    sex = Field()
    dateOfBirth = Field()
    dateOfDeath = Field()
    countryOfBirth = Field()
    countryOfStanding = Field()
    size = Field()
    weight = Field()
    colour = Field()
    coat = Field()
    hipScore = Field()
    elbowScore = Field()
    distinguishingFeatures = Field()
    titles = Field()
    regNo = Field()
    chipNo = Field()
    img = Field()

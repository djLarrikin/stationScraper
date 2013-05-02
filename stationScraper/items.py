# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class StationScraperItem(Item):
    # define the fields for your item here like:
    # name = Field()
    line = Field()
    station_name = Field()
    station_name_jp = Field()
    number = Field()
    location = Field()

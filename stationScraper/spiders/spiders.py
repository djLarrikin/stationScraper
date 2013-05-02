from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

from w3lib.html import remove_tags

from stationScraper.items import StationScraperItem

class WikiTableScraper(BaseSpider):
    name = "wiki"
    allowed_domains = ['wikipedia.org']
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        stations = hxs.select("//body//table[@class='wikitable']//tr")
        for station in stations:
            item = StationScraperItem()
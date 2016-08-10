from scrapy.spiders import Spider
from scrapy.selector import Selector
import os

class Spider4DSingapore(Spider):
    name = "singapore"
    start_urls = (
        "http://singapore.check4d.com/",
        # Add more 4d site here
    )

    def parse(self, response):
        filepath = os.getenv("HOME") + '/desktop/' + self.name
        sabah = Selector(response)
        outerboxs = sabah.xpath('//div[@class="outerbox"]')
        # create new file
        fileout = open(filepath, 'w')
        fileout.write("""<div class="empty-content"></div><div class="tbl"><table cellspacing="5" cellpadding="0" align="center"><tbody><tr valign="top"><td>""")
        fileout.close()
        # Open file as append and then write first two outerbox block
        fileout = open(filepath, 'a')
        fileout.write(outerboxs[0].extract())
        # Close tags
        fileout.write("""</td></tr></tbody></table></div><div class="empty-content"></div><div class="tbl"><table cellspacing="5" cellpadding="0" align="center"><tbody><tr valign="top"><td>""")
        # write next outerbox block
        fileout.write(outerboxs[1].extract())
        # closing it's tags
        fileout.write("""</td></tr></tbody></table></div><div class="clear"></div>""")
        fileout.close()

from datetime import datetime
from urllib.parse import urlencode

import scrapy
from scrapy.exceptions import CloseSpider
from scrapy.loader import ItemLoader

from linkedin_jobs_scraper.items.jobs import JobsItem


class JobsScraper(scrapy.Spider):
    name = "jobs_scraper"
    url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?"
    handle_httpstatus_list = [400]

    def start_requests(self):

        self.params = {
            "start": 1,
            "keywords": self.settings.get("KEYWORDS"),
            "location": self.settings.get("LOCATION"),
            "f_TPR": self._days_to_seconds(self.settings.get("PAST_DAYS", 1)),
        }

        yield scrapy.Request(url=self.url+urlencode(self.params), callback=self.parse)

    def parse(self, response):
        if response.status == 400:
            raise CloseSpider("Scrape finish")

        tags = response.xpath('//*[@data-entity-urn]')

        if not tags:
            raise CloseSpider("No jobs found")

        for id in tags:
            item = ItemLoader(item=JobsItem())
            item.add_value("job_id", id.attrib['data-entity-urn'])
            item.add_value("extracted_at", datetime.now().isoformat())
            yield item.load_item()

        # Paginate
        self.params["start"] += 25
        yield response.follow(url=self.url+urlencode(self.params), callback=self.parse)

    def _days_to_seconds(self, days):
        return f"r{int(days) * 86400}"

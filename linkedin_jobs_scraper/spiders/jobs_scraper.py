from pathlib import Path

import scrapy
from scrapy.http import Request


class JobsScraper(scrapy.Spider):
    name = "jobs_scraper"
    url = "https://www.linkedin.com/jobs/search/"
    handle_httpstatus_list = [400]
    page_number = 1

    def start_requests(self):
        self.payload = {
            "keywords": 'Data Engineer',  # self.keyword,
            "location": 'Canada',  # self.location,
            "trk": "public_jobs_jobs-search-bar_search-submit",
            "start": self.page_number
        }

        yield scrapy.Request(url=self.url, callback=self.parse, meta=self.payload)

    def parse(self, response):
        if response.status == 400 or self.payload["start"] > 100:
            self.close(spider=self, reason="Scrape finish")

        tags = response.xpath('//*[@data-entity-urn]')
        if not tags:
            self.close(spider=self, reason="No jobs found")

        for id in tags:
            try:
                yield {
                    "job_id": id.attrib['data-entity-urn'].split(":")[-1]
                }
            except Exception as e:
                self.log(e)

        # Pagination
        self.payload["start"] += 25
        # yield Request(url="https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Data%20Engineer&location=Canada&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=200&start=125", callback=self.parse)

        yield response.follow(url=self.url, callback=self.parse, meta=self.payload, dont_filter=True)

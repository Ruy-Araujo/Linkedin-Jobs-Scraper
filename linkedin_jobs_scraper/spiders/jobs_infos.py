from datetime import datetime
import time

import scrapy
from scrapy.loader import ItemLoader
from scrapy.exceptions import CloseSpider
from scrapy.spidermiddlewares.httperror import HttpError
from scrapy.utils.project import get_project_settings
from scrapy.utils.response import response_status_message
from twisted.internet.error import DNSLookupError, TimeoutError, TCPTimedOutError

from linkedin_jobs_scraper.items.jobs_infos import JobsInfosItem


def parse_load(cookies: str) -> dict:
    """Parse cookies from string to dict"""
    return {c[0]: c[1] for c in [cookies.split("=", 1) for cookies in cookies.split(";")]}


class JobsInfosScraper(scrapy.Spider):
    name = "jobs_infos_scraper"
    url = "https://www.linkedin.com/voyager/api/jobs/jobPostings/"

    def start_requests(self):
        self.job_id = iter(self.jobs_ids)
        self.cookies = parse_load(self.settings.get("LINKEDIN_COOKIES"))
        self.headers = {
            "csrf-token": self.settings.get("CSRF_TOKEN"),
        }

        yield scrapy.Request(url=self.url + next(self.job_id), callback=self.parse, cookies=self.cookies, headers=self.headers)

    def parse(self, response):
        json_response = response.json()

        item = ItemLoader(item=JobsInfosItem())
        item.add_value("job_id", json_response['jobPostingId'])
        item.add_value("data", json_response)
        item.add_value("extracted_at", datetime.now().isoformat())
        yield item.load_item()

        next_job = next(self.job_id, None)

        if not next_job:
            raise CloseSpider("No more results, scrapy stoped...")

        yield response.follow(url=self.url + next_job, callback=self.parse, cookies=self.cookies, headers=self.headers)

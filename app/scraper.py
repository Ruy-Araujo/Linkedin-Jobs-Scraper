import logging
import requests
from bs4 import BeautifulSoup


class Scraper:

    def __init__(self, keyword, location):
        self.url = "https://www.linkedin.com"
        self.keyword = keyword
        self.location = location
        self._session = self._init_session()
        self.jobs_ids = []

    def _init_session(self):

        hearders = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        }

        session = requests.Session()
        session.headers.update(hearders)
        return session

    def search_jobs(self, page=0):
        path = "/jobs/search/"

        payload = {
            "keywords": self.keyword,
            "location": self.location,
            "trk": "public_jobs_jobs-search-bar_search-submit",
            "position": 1,
            "pageNum": page
        }

        response = self._session.get(self.url + path, params=payload)
        return response

    def parse_response(self, response):

        soup = BeautifulSoup(response.text, "html.parser")

        job_cards = soup.find_all(
            "div", {"class": "base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card"})

        if not job_cards:
            logging.info("No jobs found")
            return None

        for job_card in job_cards:
            try:
                self.jobs_ids.append(job_card["data-entity-urn"].split(":")[-1])
            except:
                continue

        return self.jobs_ids

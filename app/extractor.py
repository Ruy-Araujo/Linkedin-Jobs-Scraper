import requests
import logging
from datetime import datetime


class Extractor:

    def __init__(self, cookies, csrf_token):
        self.url = "https://www.linkedin.com/voyager/api/jobs/jobPostings/"
        self._cookies = cookies
        self._csrf_token = csrf_token
        self._session = self._init_session()

    def _init_session(self):

        hearders = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "csrf-token": self._csrf_token,
        }

        session = requests.Session()
        session.headers.update(hearders)

        for cookie in self._load_cookies():
            session.cookies.set(cookie[0], cookie[1])

        return session

    def _load_cookies(self):
        cookies = self._cookies.split(";")
        return [tuple(cookie.split("=", 1)) for cookie in cookies]

    def job_details(self, job_id):
        logging.info(f"Extracting job details for job id {job_id}...")

        max_attempts = 3
        while max_attempts > 0:

            try:
                response = self._session.get(self.url + job_id)
                data = response.json()
                return data.update({"extracted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            except Exception as e:
                logging.error(f"Error while extracting job details for job id {job_id}: {e} retrying...")
                max_attempts -= 1
        return None

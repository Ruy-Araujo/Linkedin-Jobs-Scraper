import logging
import os
import time
from dotenv import load_dotenv
from ratelimiter import RateLimiter

from app.scraper import Scraper
from app.extractor import Extractor

load_dotenv()
logging.basicConfig(level=logging.INFO)


logging.info("Starting application...")


def limited(until):
    duration = int(round(until - time.time()))
    print('Rate limited, sleeping for {:d} seconds'.format(duration))


def get_jobs_ids():
    logging.info("Scraping jobs ids...")

    page = 0
    jobs_ids = []
    scrap = Scraper(
        os.getenv("QUERY"),
        os.getenv("LOCATION"))

    while len(jobs_ids) <= int(os.getenv("MAX_RESULTS")):
        results = scrap.search_jobs(page)
        jobs = scrap.parse_response(results)

        if not jobs:
            break

        jobs_ids.extend(jobs)
        page += 1

    return jobs_ids


def get_jobs_details(jobs_ids):
    logging.info("Extracting jobs details...")

    jobs_details = []
    max_calls = int(os.getenv("MAX_CALLS")) if os.getenv("MAX_CALLS") else 1
    sleep_time = int(os.getenv("SLEEP_TIME")) if os.getenv("SLEEP_TIME") else 60
    extract = Extractor(os.getenv("COOKIES"), os.getenv("CSRF_TOKEN"))
    rate_limiter = RateLimiter(max_calls=max_calls, period=sleep_time, callback=limited)

    for job_id in jobs_ids:
        with rate_limiter:
            jobs_details.append(extract.job_details(job_id))
    return jobs_details


def main():
    jobs_ids = get_jobs_ids()
    jobs_datails = get_jobs_details(jobs_ids)

    print(jobs_datails)


main()

import uuid
import json
import argparse

from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from twisted.internet import task

from linkedin_jobs_scraper.spiders.jobs import JobsScraper
from linkedin_jobs_scraper.spiders.jobs_infos import JobsInfosScraper

# Arguments
parser = argparse.ArgumentParser(description='This is a LinkedIn jobs scraper')
parser.add_argument('--keywords', type=str, help='string with the keywords that will be used to filter job listings')
parser.add_argument('--location', type=str, help='string with the location where the job listings will be searched')
parser.add_argument('--pastdays', type=int, help='integer with the number of days to look back for job listings')

# Spider settings
configure_logging()
base_settings = {
    "FEED_FORMAT": "json",
    "FEED_EXPORTERS": {
        "json": "scrapy.exporters.JsonItemExporter",
    },
}


def get_ids(pipeline):
    settings = get_project_settings()
    settings.update({**base_settings, "FEED_URI": f"tmp/{pipeline}.json"})
    return settings


def get_infos(result, runner):
    args = parser.parse_args()
    settings = get_project_settings()
    location = args.location if args.location else settings.get("LOCATION")
    keywords = args.keywords if args.keywords else settings.get("KEYWORDS")
    past_days = args.pastdays if args.pastdays else settings.get("PAST_DAYS")
    runner.settings.update({
        **base_settings,
        "FEED_URI": f"data/{location}/{keywords}/%(time)s_jobs_data.json",
        "KEYWORDS": keywords,
        "LOCATION": location,
        "PAST_DAYS": past_days,
    })

    return runner.crawl(JobsInfosScraper, jobs_ids=result)


def load_ids(_, pipeline):
    with open(f"tmp/{pipeline}.json", "r") as file:
        file = json.load(file)

    return [item["job_id"] for item in file]


def main(reactor):
    pipeline_id = str(uuid.uuid4())
    runner = CrawlerRunner(get_ids(pipeline_id))
    d = runner.crawl(JobsScraper)
    d.addCallback(load_ids, pipeline_id)
    d.addCallback(get_infos, runner)
    return d


task.react(main)

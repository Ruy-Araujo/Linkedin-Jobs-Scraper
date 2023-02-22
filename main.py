import uuid
import json

from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from twisted.internet import task

from linkedin_jobs_scraper.spiders.jobs import JobsScraper
from linkedin_jobs_scraper.spiders.jobs_infos import JobsInfosScraper

base_settings = {
    "FEED_FORMAT": "json",
    "FEED_EXPORTERS": {
        "json": "scrapy.exporters.JsonItemExporter",
    },
}

configure_logging()


def get_ids(pipeline):
    settings = get_project_settings()
    settings.update({**base_settings, "FEED_URI": f"tmp/{pipeline}.json"})
    return settings


def get_infos(result, runner):
    settings = get_project_settings()
    location = settings.get("LOCATION")
    keywords = settings.get("KEYWORDS")
    runner.settings.update({**base_settings,
                            "FEED_URI": f"data/{location}/{keywords}/%(time)s_jobs_data.json"})

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

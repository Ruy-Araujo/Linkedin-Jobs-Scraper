# Scrapy settings for linkedin_jobs_scraper project
BOT_NAME = "linkedin_jobs_scraper"

SPIDER_MODULES = ["linkedin_jobs_scraper.spiders"]
NEWSPIDER_MODULE = "linkedin_jobs_scraper.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 60/40.0
RANDOMIZE_DOWNLOAD_DELAY = False
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 10
CONCURRENT_REQUESTS_PER_IP = 15

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
# TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
TWISTED_REACTOR = "twisted.internet.epollreactor.EPollReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Custom Settings
LINKEDIN_COOKIES = 'your_cookies'
CSRF_TOKEN = 'your_csrf_token'

# Search parameters
KEYWORDS = 'Data Engineer'
LOCATION = 'Canada'

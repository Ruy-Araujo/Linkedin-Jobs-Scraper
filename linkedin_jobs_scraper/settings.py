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
DOWNLOAD_DELAY = 60/15.0
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
LINKEDIN_COOKIES = 'lang=v=2&lang=pt-br; bcookie="v=2&fa3fe7db-5852-4dd6-8f36-056534acbc3a"; bscookie="v=1&202302220310372e9c3cd6-cc49-4a41-8e54-d88d5d09734cAQGCu0MSgKgVPuvACECjklptur-_fHA3"; AMCVS_14215E3D5995C57C0A495C55@AdobeOrg=1; liap=true; li_at=AQEDASnVKtEFmk4iAAABhncai-MAAAGGmycP41YA0WYj-MgoxsHdMpLcdZIuLD4_-XC5YihZyJpiLjy7NcsI-Q_etqjet0Xf4S4IQ3jHq-pm0BcgXy2qcERx1T28q4_2RVMZSUvEaa6xWhA3uB0yBks1; JSESSIONID="ajax:6462774306453345227"; timezone=America/Sao_Paulo; li_theme=light; li_theme_set=app; li_sugr=9afd7a16-9aa5-4585-a6f5-0d399723749a; _guid=77e6937d-5a98-4df1-8273-af40a953f002; _gcl_au=1.1.1933519934.1677035689; AnalyticsSyncHistory=AQJ6Snuu_yNo8gAAAYaQK3dW5Gp2ZfuuZo3YFQrLZTIpApVtscU0BMmFvr6ZMDX4SFNYAjE7pxNDcWU0ibqFpw; lms_ads=AQEXUSMK9K1DDwAAAYaQK3g-lTiVbEA9IduHvjmHht8LEdUH5Vzgc9Xw1XJeE5WKsYRs4m5v8MAelkdDPzaTwW3kC5m0DZSe; lms_analytics=AQEXUSMK9K1DDwAAAYaQK3g-lTiVbEA9IduHvjmHht8LEdUH5Vzgc9Xw1XJeE5WKsYRs4m5v8MAelkdDPzaTwW3kC5m0DZSe; UserMatchHistory=AQJshy300SQtIwAAAYaQMA6ZYS__HQqJLtE9tpHORgZ6C9G18z0b0zoeyJ3mbCvlNEia6HL6aRKOeOLwA0kRqBN5xS9DC13dtcUhgHcsi9dYo16sNM-TiPpg3-lXrYHlqKZ8FfVTI--d0MHSdk9AXNgLhA0vgnggaTnytB82vk9pp_XYqDztx7yD-yK2VY-JSqJ30WWXPfyWIaz-wh5WMkqgVLVlD_5M7VDmui9dRECTrdUqnA5z6zKMmLAxmRGpUeigdsA83sx0PAOwmU4uTz-mtCm9iSaitdyK8c8; lidc="b=VP00:s=V:r=V:a=V:p=V:g=284:u=423:x=1:i=1677456315:t=1677456528:v=2:sig=AQGijQfAHtA81RkpUeOF4Wm2AQfxGfi2"; AMCV_14215E3D5995C57C0A495C55@AdobeOrg=-637568504|MCIDTS|19416|MCMID|20266348116775381982951441394686842485|MCOPTOUT-1677463517s|NONE|vVersion|5.1.1; sdsc=22:1,1677456378973~JAPP,0UyVpMHIyynHJHIiR4+aPWNzihpM='
CSRF_TOKEN = 'ajax:6462774306453345227'

# Search parameters
KEYWORDS = 'Data Engineer'
LOCATION = 'Canada'
PAST_DAYS = 7

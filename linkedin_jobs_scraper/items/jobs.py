# from dataclasses import dataclass

from scrapy.item import Item, Field
# from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst


def extract_job_id(value):
    return value.split(":")[-1]


class JobsItem(Item):
    job_id = Field(input_processor=MapCompose(extract_job_id), output_processor=TakeFirst())
    extracted_at = Field(output_processor=TakeFirst())

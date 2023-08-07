# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, Compose, TakeFirst

def process_price(price):
    try:
        price = int(''.join(price[2]))
    except Exception as e:
        # print(e)
        pass
    return price

def process_name(name):
    try:
        name = name[0].replace('\n','').strip()
    except Exception as e:
        # print(e)
        pass
    return name

def process_photos(photos):
    try:
        photos = ["https://castorama.ru" + photo for photo in photos if photo[0] == "/"]
    except Exception as e:
        # print(e)
        pass
    return photos


class CastoramaItem(scrapy.Item):
    name = scrapy.Field(input_processor=process_name(process_price), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=Compose(process_price), output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=Compose(process_photos), output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())

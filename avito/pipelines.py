# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class AvitoparserPipeline:
    def process_item(self, item, spider):
        return item


class ItemPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item):
        if item['photos']:
            for photo in item['photos']:
                try:
                    yield scrapy.Request(photo)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item):
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        return item
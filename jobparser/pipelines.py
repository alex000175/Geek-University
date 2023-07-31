# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class JobparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.vacancy3007

    def process_item(self, item, spider):
        # обработка данных
        item['salary_min'] = self.get_payment_min(' '.join(item['salary']))
        item['salary_max'] = self.get_payment_max(' '.join(item['salary']))
        
        del item['salary']
        # запись в БД
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item
    
    def get_payment_min(self, s):
        if s.rfind('от')>=0:
            res = ''.join(filter(lambda i: i.isdigit(), s))
            return int(res)
        
        if s.rfind('–')>=0:
            res = s.split('–')[0]
            res = ''.join(filter(lambda i: i.isdigit(), res))
            return int(res)
    
    def get_payment_max(self, s):
        if s.rfind('до')>=0:
            res = ''.join(filter(lambda i: i.isdigit(), s))
            return int(res)
        
        if s.rfind('–')>=0:
            res = s.split('–')[1]
            res = ''.join(filter(lambda i: i.isdigit(), res))
            return int(res)

from pymongo import MongoClient
from form.settings import MONGO_URL, MONGO_DB, MONGO_COLLECTION


class MongoRepo:
    def __init__(self, mongo_db=MONGO_DB, mongo_collection=MONGO_COLLECTION):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[mongo_db]
        self.collection = self.db[mongo_collection]

    def read_docs_from_collection(self):
        documents = self.collection.find()
        for document in documents:
            yield document

    def find_element(self, data):
        return self.collection.find_one(data)

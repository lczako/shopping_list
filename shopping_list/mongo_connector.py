import json
import os
from pymongo import MongoClient


class MongoDBConnector:

    DB_NAME = 'app_db'
    RECIPIES_COLLECTION_NAME = 'recipies'
    RECIPIES_COLLECTION_SCHEMA_PATH = os.getenv('APP_HOME')+'/src/collection_recipies_schema.json'
    RECIPIES_ARCHIVE_PATH = os.getenv('APP_HOME')+'/src/recipies.json'
    SHOPPING_LISTS_COLLECTION_NAME = 'shopping_lists'

    def __init__(self):
        print(f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@mongo")
        self.client = MongoClient(f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@mongo")

    @property
    def db(self):
        return self.client[self.DB_NAME]

    @property
    def recipies(self):
        return self.db[self.RECIPIES_COLLECTION_NAME]

    @property
    def shopping_list(self):
        return self.db[self.SHOPPING_LISTS_COLLECTION_NAME]

    def init_app_db(self):
        print("Initializing app database")
        coll_names = self.db.list_collection_names()
        if self.SHOPPING_LISTS_COLLECTION_NAME not in coll_names:
            self.db.create_collection(self.SHOPPING_LISTS_COLLECTION_NAME)
        if self.RECIPIES_COLLECTION_NAME not in coll_names or self.db[self.RECIPIES_COLLECTION_NAME].count_documents({}) == 0:
            print("Have not found Recipies in the database, creating it from archives.")
            self.init_recipies()
        return

    def init_recipies(self):
        if self.RECIPIES_COLLECTION_NAME not in self.db.list_collection_names():
            self.db.create_collection(self.RECIPIES_COLLECTION_NAME)

        with open(self.RECIPIES_COLLECTION_SCHEMA_PATH) as f:
            schema = json.load(f)
        self.db.command('collMod', self.RECIPIES_COLLECTION_NAME, validator=schema, validationLevel='strict')

        with open(self.RECIPIES_ARCHIVE_PATH) as f:
            data = json.load(f)
        self.db[self.RECIPIES_COLLECTION_NAME].insert_many(data)
        return

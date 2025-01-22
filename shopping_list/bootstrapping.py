from argparse import ArgumentParser
from mongo_connector import MongoDBConnector

mdc = MongoDBConnector()
mdc.init_app_db()
print(mdc.DB_NAME, " is ready to use.")

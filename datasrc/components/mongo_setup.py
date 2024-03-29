import os
import sys
from datasrc.utils.database_handler import MongodbClient
from datasrc.exception.custom_exception import DataException
class MetaDataStore:
    def __init__(self):
        self.root = os.path.join(os.getcwd(), "data")
        self.images = os.path.join(self.root, "images-101")
        self.labels = os.listdir(self.images)
        self.mongo = MongodbClient()

    def register_labels(self):
        try:
            records = {}
            for num, label in enumerate(self.labels):
                records[f"{num}"] = label

            self.mongo.database['labels'].insert_one(records)

        except Exception as e:
            message = DataException(e, sys)
            return {"Created": False, "Reason": message.error_message}

    def run_step(self):
        try:
            self.register_labels()
        except Exception as e:
            message = DataException(e, sys)
            return {"Created": False, "Reason": message.error_message}


if __name__ == "__main__":
    meta = MetaDataStore()
    meta.run_step()

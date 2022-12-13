import pymongo
import os


class MongodbClient:
    client = None

    def __init__(self, database_name=os.environ["DATABASE_NAME"]) -> None:
        if MongodbClient.client is None:
            MongodbClient.client = pymongo.MongoClient(
                f"mongodb+srv://{os.environ['MONGO_CLUSTER_USERNAME']}:{os.environ['MONGO_CLUSTER_PASSWORD']}@projects.ch4mixt.mongodb.net/?retryWrites=true&w=majority"
            )
        self.client = MongodbClient.client
        self.database = self.client[database_name]
        self.database_name = database_name
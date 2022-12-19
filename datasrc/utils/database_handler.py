import pymongo
import os


class MongodbClient:
    client = None

    def __init__(self, database_name=os.environ["MONGO_DATABASE_NAME"]) -> None:
        if MongodbClient.client is None:
            MongodbClient.client = pymongo.MongoClient(
                f"mongodb+srv://{os.environ['MONGO_ATLAS_CLUSTER_USERNAME']}:{os.environ['MONGO_ATLAS_CLUSTER_PASSWORD']}@imagesecluster.pemlurn.mongodb.net/?retryWrites=true&w=majority"
            )
        self.client = MongodbClient.client
        self.database = self.client[database_name]
        self.database_name = database_name


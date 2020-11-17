"""
Pipeline of saving data to MongoDB
"""
import pprint

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)

from sensor_reader.base import BaseComponent
from sensor_reader.signals import Signal


class MongoDBPipeline(BaseComponent):
    """
    Pipeline of saving data to MongoDB
    """

    name = "MongoDBPipeline"
    setting_prefix = "MONGODB_PIPELINE_"

    client: AsyncIOMotorClient
    db: AsyncIOMotorDatabase
    collection: AsyncIOMotorCollection

    async def start(self, signal: Signal, sender) -> None:
        """

        :param signal:
        :type signal: Signal
        :param sender:
        :type sender:
        :return:
        :rtype: None
        """
        self.client = AsyncIOMotorClient(self.config["MONGODB_URL"])

        server_info = await self.client.server_info()

        del server_info["buildEnvironment"]

        self.logger.info(
            "MongoDB [%s:%s] is connected:\n%s",
            *self.client.address,
            pprint.pformat(server_info),
        )

        self.db = self.client.get_database(self.config["MONGODB_DATABASE"])
        self.collection = self.db[self.config["MONGODB_COLLECTION"]]

    async def process_item(self, item):
        """

        :param item:
        :return:
        """
        await self.collection.insert_many(item)
        return item

    async def stop(self, signal: Signal, sender) -> None:
        """

        :param signal:
        :type signal: Signal
        :param sender:
        :return:
        :rtype: None
        """
        self.logger.info("MongoDB [%s:%s] is disconnected", *self.client.address)
        self.client.close()

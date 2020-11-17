"""
Pipeline of saving data to MongoDB
"""
import pprint

from motor.motor_asyncio import AsyncIOMotorClient

from sensor_reader.base import BaseComponent
from sensor_reader.signals import Signal


class MongoDBPipeline(BaseComponent):
    """
    Pipeline of saving data to MongoDB
    """

    name = "MongoDBPipeline"
    setting_prefix = "MONGODB_PIPELINE_"

    client: AsyncIOMotorClient

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

    async def process_item(self, item):
        """

        :param item:
        :return:
        """
        # TODO: receive value and save to database
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

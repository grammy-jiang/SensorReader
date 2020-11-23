"""
Pipeline of saving data to MongoDB
"""
from __future__ import annotations

import pprint
import struct
from datetime import datetime

from bson.objectid import _MAX_COUNTER_VALUE
from bson.objectid import ObjectId as _ObjectId
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)

from sensor_reader.base import BaseComponent
from sensor_reader.signals import Signal


class ObjectId(_ObjectId):
    @classmethod
    def from_datetime(cls, generation_time: datetime) -> ObjectId:
        """

        :param generation_time:
        :type generation_time: datetime
        :return:
        :rtype: ObjectId
        """
        # 4 bytes current time
        oid = struct.pack(">I", int(generation_time.timestamp()))

        # 5 bytes random
        oid += ObjectId._random()

        # 3 bytes inc
        with ObjectId._inc_lock:
            oid += struct.pack(">I", ObjectId._inc)[1:4]
            ObjectId._inc = (ObjectId._inc + 1) % (_MAX_COUNTER_VALUE + 1)

        return _ObjectId(oid)


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
        _item = []
        for item_ in item:
            _ = {}
            for key, value in item_.items():
                if key == "timestamp":
                    _["_id"] = ObjectId.from_datetime(item_["timestamp"])
                else:
                    _[key] = value
            _item.append(_)

        await self.collection.insert_many(_item)
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

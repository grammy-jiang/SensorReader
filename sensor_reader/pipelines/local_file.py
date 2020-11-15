"""
Pipeline of saving data to PostgreSQL
"""
import pprint

import aiofiles

from sensor_reader.base import BaseComponent
from sensor_reader.signals import Signal


class LocalFilePipeline(BaseComponent):
    """
    Pipeline of saving data to PostgreSQL
    """

    name = "LocalFilePipeline"
    setting_prefix = "LOCAL_FILE_PIPELINE_"

    file: aiofiles.threadpool.text.AsyncTextIOWrapper

    async def start(self, signal: Signal, sender) -> None:
        """

        :param signal:
        :type signal: Signal
        :param sender:
        :type sender:
        :return:
        :rtype: None
        """
        self.file = await aiofiles.open(self.config["FILE"], "w")

    async def process_item(self, item):
        """

        :param item:
        :return:
        """
        await self.file.write(f"{pprint.pformat(item)}\n")
        return item

    async def stop(self, signal: Signal, sender) -> None:
        """

        :param signal:
        :type signal: Signal
        :param sender:
        :return:
        :rtype: None
        """
        self.logger.info("PostgreSQL is disconnected")
        await self.file.close()

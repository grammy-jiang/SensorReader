"""
Pipeline of saving data to PostgreSQL
"""
import pprint

from aiofile import BinaryFileWrapper, async_open

from sensor_reader.base import BaseComponent
from sensor_reader.signals import Signal


class LocalFilePipeline(BaseComponent):
    """
    Pipeline of saving data to PostgreSQL
    """

    name = "LocalFilePipeline"
    setting_prefix = "LOCAL_FILE_PIPELINE_"

    file: BinaryFileWrapper

    async def start(self, signal: Signal, sender) -> None:
        """

        :param signal:
        :type signal: Signal
        :param sender:
        :type sender:
        :return:
        :rtype: None
        """
        self.file = async_open(self.config["FILE"], "w")

    async def process_item(self, item):
        """

        :param item:
        :return:
        """
        await self.file.write(pprint.pformat(item))
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

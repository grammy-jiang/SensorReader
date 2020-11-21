"""
Channel Manager
"""
import asyncio
import pprint
from functools import cached_property, partial
from typing import Dict, List

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from sensor_reader.base import BaseComponent
from sensor_reader.signals import Signal
from sensor_reader.utils import load_object


class ChannelManager(BaseComponent):
    """
    Channel Manager
    """

    manage = "CHANNELS"
    name = "ChannelManager"
    setting_prefix = "CHANNELS_MANAGER_"

    def __init__(self, service, name: str = None, setting_prefix: str = None):
        """

        :param service:
        :type service:
        :param name:
        :type name: str
        :param setting_prefix:
        :type setting_prefix: str
        """
        super().__init__(service, name, setting_prefix)

        self.stats = service.stats
        self.channels: Dict = {}
        self._initialize_channels()

        self.logger.info("Enabled channels:\n%s", pprint.pformat(self.cls_channels))

        self.scheduler = AsyncIOScheduler()

    @cached_property
    def cls_channels(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Get all extensions with the priority in a dict
        :return:
        :rtype: Dict[str, int]
        """
        return self.settings[self.manage]

    def get_channel(self, name: str) -> object:
        """
        Get an extension by its name
        :param name:
        :type name: str
        :return:
        :rtype: object
        """
        return self.channels[name]

    def _initialize_channels(self) -> None:
        """

        :return:
        :rtype: None
        """
        for key, value in self.cls_channels.items():
            readers = [
                load_object(cls_readers).from_service(self.service)
                for cls_readers in value["readers"]
            ]

            pipelines = [
                load_object(cls_pipelines).from_service(self.service)
                for cls_pipelines in value["pipelines"]
            ]

            self.channels[key] = {"readers": readers, "pipelines": pipelines}

    async def start(self, signal: Signal, sender) -> None:
        """

        :param signal:
        :type signal: Signal
        :param sender:
        :type sender:
        :return:
        :rtype: None
        """

        for name, channel in self.channels.items():
            job = partial(
                self.process_channel,
                readers=channel["readers"],
                pipelines=channel["pipelines"],
            )
            self.scheduler.add_job(
                job,
                "cron",
                **self.config["CHANNEL_SENSE_HAT_SCHEDULE"],
            )

    async def stop(self, signal: Signal, sender):
        """

        :param signal:
        :type signal: Signal
        :param sender:
        :type sender:
        :return:
        :rtype:
        """
        self.scheduler.shutdown()

    async def process_channel(self, readers: List, pipelines: List) -> None:
        """

        :param readers:
        :type readers: List
        :param pipelines:
        :type pipelines: List
        :return:
        :rtype: None
        """
        results: List = await asyncio.gather(*(reader.read() for reader in readers))
        self.stats.increase("items")
        self.logger.debug(
            "From readers get the following results:\n%s", pprint.pformat(results)
        )

        for pipeline in pipelines:
            results = await pipeline.process_item(results)

    async def start_channels(self) -> None:
        """

        :return:
        :rtype: None
        """
        self.scheduler.start()

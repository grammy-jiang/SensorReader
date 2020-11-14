"""
Channel Manager
"""
import asyncio
import pprint
from functools import cached_property
from typing import Dict, List

from sensor_reader.base import BaseComponent
from sensor_reader.pipelines import PostgreSQLPipeline
from sensor_reader.readers import SensorHATReader
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

        self.channels: Dict = {}
        self._initialize_channels()

        self.logger.info("Enabled channels:\n%s", pprint.pformat(self.cls_channels))

    @classmethod
    def from_service(cls, service, name: str = None, setting_prefix: str = None):
        """
        Initialize components from a service instance
        :param service:
        :type service:
        :param name:
        :type name: str
        :param setting_prefix:
        :type setting_prefix: str
        :return:
        """
        obj = cls(service, name, setting_prefix)

        return obj

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

    async def start_channels(self, signal: Signal, sender) -> None:
        """

        :param signal:
        :type signal: Signal
        :param sender:
        :type sender:
        :return:
        :rtype: None
        """

        loop = asyncio.get_event_loop()

        for key, value in self.channels.items():
            reader: SensorHATReader
            for reader in value["readers"]:
                loop.create_task(reader.start_reading(signal, sender))
            pipeline: PostgreSQLPipeline
            for pipeline in value["pipelines"]:
                loop.create_task(pipeline.start_piping(signal, sender))

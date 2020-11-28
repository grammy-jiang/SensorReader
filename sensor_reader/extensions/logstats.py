"""
LogStats
"""
from asyncio.events import TimerHandle
from functools import cached_property

from sensor_reader.base import BaseComponent
from sensor_reader.signals import Signal


class LogStats(BaseComponent):
    """
    Log basic stats periodically
    """

    name: str = "LogStats"
    setting_prefix: str = "LOGSTATS_"

    timer_handle: TimerHandle

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

        self.loop = service.loop

        self._no_read: int = 0  # number of read

    @cached_property
    def stats(self):
        return self.service.stats

    async def start(self, signal: Signal, sender) -> None:
        """

        :param signal:
        :type signal: Signal
        :param sender:
        :type sender:
        :return:
        :rtype: None
        """
        self.log()

    async def stop(self, signal: Signal, sender) -> None:
        """

        :param signal:
        :type signal: Signal
        :param sender:
        :type sender:
        :return:
        :rtype: None
        """
        if self.timer_handle:
            self.timer_handle.cancel()

    def log(self) -> None:
        """

        :return:
        :rtype: None
        """
        self.logger.info(
            "Item read: [%s/%s]",
            self.stats["items"] - self._no_read,
            self.stats["items"],
        )
        self._no_read = self.stats["items"]

        self.timer_handle = self.loop.call_later(
            self.config["INTERVAL"], self.log
        )

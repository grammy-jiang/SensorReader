"""
LogStats
"""
from asyncio.events import TimerHandle, get_event_loop

from sensor_reader.base import BaseComponent
from sensor_reader.signals import Signal


class LogStats(BaseComponent):
    """
    Log basic stats periodically
    """

    name: str = "LogStats"
    setting_prefix: str = "LOGSTATS_"

    timer_handle: TimerHandle

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
        # TODO: add the log message

        loop = get_event_loop()
        self.timer_handle = loop.call_later(self.config["INTERVAL"], self.log)

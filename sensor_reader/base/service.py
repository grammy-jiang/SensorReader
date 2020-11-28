"""
Base class of Service
"""
from __future__ import annotations

import asyncio
from signal import SIGHUP, SIGINT, SIGQUIT, SIGTERM

from sensor_reader.settings import Settings
from sensor_reader.utils import LoggerMixin, configure_event_loop


class BaseService(LoggerMixin):
    """
    Base class of Service
    """

    def __init__(self, settings: Settings):
        """

        :param settings:
        :type settings: Settings
        """
        self.settings = settings
        configure_event_loop(self.settings)
        self.loop = asyncio.get_event_loop()

        signals = (SIGHUP, SIGQUIT, SIGTERM, SIGINT)

        for signal in signals:
            self.loop.add_signal_handler(
                signal,
                lambda s=signal: asyncio.create_task(self.stop(s)),
            )

    @classmethod
    def from_settings(cls, settings: Settings) -> BaseService:
        """

        :param settings:
        :type settings: Settings
        :return:
        :rtype: BaseService
        """
        obj = cls(settings)

        return obj

    def start(self) -> None:
        """

        :return:
        :rtype None
        """
        self.loop.run_forever()
        self.loop.close()

    async def stop(self, signal=None) -> None:  # pylint: disable=unused-argument
        """

        :param signal:
        :type signal:
        :return:
        :rtype: None
        """
        self.loop.stop()

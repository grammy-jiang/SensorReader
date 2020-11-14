"""
Signal Manager (Dispatcher)
"""
from __future__ import annotations

import asyncio
import functools
import pprint
from collections import UserDict
from typing import Callable, Set

from sensor_reader.settings import Settings
from sensor_reader.utils import LoggerMixin


class SignalManager(UserDict, LoggerMixin):  # pylint: disable=too-many-ancestors
    """
    Signal Manager
    """

    name: str = "SignalManager"
    setting_prefix: str = "SIGNAL_MANAGER_"

    def __init__(self, settings, name: str = None, setting_prefix: str = None):
        """

        :param settings:
        :type settings:
        :param name:
        :type name: str
        :param setting_prefix:
        :type setting_prefix: str
        """
        super().__init__()

        self.settings = settings

        if name:
            self.name = name

        if setting_prefix:
            self.setting_prefix = setting_prefix

    def __missing__(self, key: object) -> Set:
        self[key] = set()
        return self[key]

    @classmethod
    def from_settings(
        cls, settings: Settings, name: str = None, setting_prefix: str = None
    ) -> SignalManager:
        """

        :param settings:
        :type settings: Settings
        :param name:
        :type name: str
        :param setting_prefix:
        :type setting_prefix: str
        :return:
        :rtype: SignalManager
        """
        obj = cls(settings, name, setting_prefix)
        return obj

    def connect(self, receiver: Callable, signal: object) -> None:
        """
        Connect a receiver to a signal.

        :param receiver:
        :type receiver: callable
        :param signal:
        :type signal: object
        :return:
        :rtype: None
        """
        self[signal].add(receiver)
        self.logger.debug(
            "Signal [%s] is added a receiver [%s]",
            signal,
            f"{receiver.__self__.__class__.__module__}."
            f"{receiver.__self__.__class__.__name__}."
            f"{receiver.__name__}",
        )

    def disconnect(self, receiver: Callable, signal: object) -> None:
        """
        Disconnect a receiver function from a signal. This has the opposite
        effect of the connect method, and the arguments are the same.

        :param receiver:
        :type receiver: Callable
        :param signal:
        :type signal: object
        :return:
        :rtype: None
        """
        self[signal].remove(receiver)
        self.logger.debug("Remove receiver [%s] from signal [%s]", receiver, signal)

    def send(self, signal: object, **kwargs) -> None:
        """
        Send a signal, catch exceptions and log them.

        The keyword arguments are passed to the signal handlers (connected
        through the connect method).

        :param signal:
        :type signal: object
        :param kwargs:
        :return:
        :rtype: None
        """
        loop = asyncio.get_event_loop()

        receiver: Callable
        for receiver in self[signal]:
            _receiver = functools.partial(receiver, signal=signal, **kwargs)
            if asyncio.iscoroutinefunction(receiver):
                loop.create_task(_receiver())
            else:
                loop.call_soon_threadsafe(_receiver)

    async def send_and_wait(self, signal: object, **kwargs) -> None:
        """

        :param signal:
        :type signal: object
        :param kwargs:
        :return:
        :rtype: None
        """
        self.logger.debug(
            "Receive a signal [%s], receivers connected:\n%s",
            signal,
            pprint.pformat(
                [
                    f"{receiver.__self__.__class__.__module__}."
                    f"{receiver.__self__.__class__.__name__}."
                    f"{receiver.__name__}"
                    for receiver in self[signal]
                ]
            ),
        )

        tasks = set()

        receiver: Callable
        for receiver in self[signal]:
            if asyncio.iscoroutinefunction(receiver):
                tasks.add(receiver(signal=signal, **kwargs))
            else:
                receiver(signal=signal, **kwargs)

        if tasks:
            await asyncio.wait(tasks)

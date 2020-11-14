"""
Sensor Reader
"""
from datetime import datetime
from functools import cached_property

from sensor_reader.base import BaseService
from sensor_reader.extensions.manager import ExtensionManager
from sensor_reader.settings import Settings
from sensor_reader.signals import (
    Signal,
    SignalManager,
    component_start,
    component_stop,
    service_start,
    service_stop,
)
from sensor_reader.utils import load_object


class SensorReaderService(BaseService):
    """
    Sensor Reader
    """

    def __init__(self, settings: Settings):
        """

        :param settings:
        :type settings: Settings
        """
        super().__init__(settings)

        self.signal_manager: SignalManager = load_object(
            settings["CLS_SIGNAL_MANAGER"]
        ).from_settings(settings)

        self.extension_manager: ExtensionManager = load_object(
            settings["CLS_EXTENSION_MANAGER"]
        ).from_service(self)

    def start(self) -> None:
        """

        :return:
        :rtype: None
        """
        self.logger.info("Start SensorReader now...")
        self.stats["time/start"] = datetime.now()

        self.logger.info("Start components now...")
        self.loop.run_until_complete(
            self.signal_manager.send_and_wait(component_start, sender=self)
        )

        self.logger.info("Start serving now...")
        self.signal_manager.connect(self._start, service_start)
        self.signal_manager.send(service_start, sender=self)

        super().start()

    async def _start(self, signal: Signal, sender) -> None:
        """

        :param signal:
        :param sender:
        :return:
        """

    async def stop(self, signal=None) -> None:
        """

        :param signal:
        :type signal:
        :return:
        :rtype: None
        """
        self.logger.info("Receive signal [%s], stop now...", signal)

        self.logger.info("Stop serving...")
        await self.signal_manager.send_and_wait(service_stop, sender=self)

        self.logger.info("Stop components...")
        await self.signal_manager.send_and_wait(component_stop, sender=self)

        await super().stop(signal)
        self.logger.info("SensorReader is stopped")

    @cached_property
    def stats(self):
        return self.extension_manager.get_extension("Stats")

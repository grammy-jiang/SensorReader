"""
Sensor Reader
"""

from sensor_reader.base import BaseService
from sensor_reader.settings import Settings
from sensor_reader.signals import SignalManager, service_stop
from sensor_reader.utils import load_object


class SensorReader(BaseService):
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

        self.logger.info("Load SignalManager from [%s]", settings["CLS_SIGNAL_MANAGER"])

    def start(self) -> None:
        """

        :return:
        :rtype: None
        """
        self.logger.info("Start SensorReader now...")
        super().start()

    async def stop(self, signal=None) -> None:
        """

        :param signal:
        :type signal:
        :return:
        :rtype: None
        """
        self.logger.info("Receive signal [%s], stop all components now...", signal)
        await self.signal_manager.send_and_wait(service_stop, sender=self)

        await super().stop(signal)
        self.logger.info("All components are stopped")

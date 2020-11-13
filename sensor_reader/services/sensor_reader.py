"""
Sensor Reader
"""

from sensor_reader.base import BaseService
from sensor_reader.settings import Settings
from sensor_reader.signals import SignalManager
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
        super().start()

    async def stop(self, signal=None) -> None:
        """

        :param signal:
        :type signal:
        :return:
        :rtype: None
        """
        await super().stop(signal)

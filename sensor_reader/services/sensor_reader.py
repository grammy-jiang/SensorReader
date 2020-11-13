"""
Sensor Reader
"""

from sensor_reader.base import BaseService
from sensor_reader.settings import Settings


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

"""
Sensor HAT Reader
"""

from sensor_reader.base import BaseComponent


class SensorHATReader(BaseComponent):
    """
    Sensor HAT Reader
    """

    name = "SensorHATReader"
    setting_prefix = "SENSOR_HAT_READER_"

    @classmethod
    def from_service(cls, service, name: str = None, setting_prefix: str = None):
        """

        :param service:
        :param name:
        :param setting_prefix:
        :return:
        """
        obj = cls(service, name, setting_prefix)

        return obj

    async def read(self):
        """

        :return:
        """

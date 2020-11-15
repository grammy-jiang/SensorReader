"""
Sensor HAT Reader
"""
from __future__ import annotations

import asyncio
from typing import Dict, Tuple

from sensor_reader.base import BaseComponent


class SensorHATReader(BaseComponent):
    """
    Sensor HAT Reader
    """

    name = "SensorHATReader"
    setting_prefix = "SENSOR_HAT_READER_"

    @classmethod
    def from_service(
        cls, service, name: str = None, setting_prefix: str = None
    ) -> SensorHATReader:
        """

        :param service:
        :param name:
        :param setting_prefix:
        :return:
        :rtype: SensorHATReader
        """
        obj = cls(service, name, setting_prefix)

        return obj

    async def read(
        self,
    ) -> Tuple[Dict[str, float], Dict[str, float], Dict[str, float], Dict[str, float]]:
        """

        :return:
        :rtype: Tuple[Dict[str, float], Dict[str, float], Dict[str, float], Dict[str, float]]
        """
        return await asyncio.gather(
            self.get_humidity(),
            self.get_temperature_from_humidity(),
            self.get_pressure(),
            self.get_temperature_from_pressure(),
        )

    async def get_humidity(self) -> Dict[str, float]:
        """

        :return:
        :rtype: Dict[str, float]
        """

    async def get_temperature_from_humidity(self) -> Dict[str, float]:
        """

        :return:
        :rtype: Dict[str, float]
        """

    async def get_pressure(self) -> Dict[str, float]:
        """

        :return:
        :rtype: Dict[str, float]
        """

    async def get_temperature_from_pressure(self) -> Dict[str, float]:
        """

        :return:
        :rtype: Dict[str, float]
        """

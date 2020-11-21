"""
Sensor HAT Reader
"""
from __future__ import annotations

import asyncio
from datetime import datetime, timedelta, timezone
from typing import Dict, Union

from sensor_reader.base import BaseComponent


class SensorHATReader(BaseComponent):
    """
    Sensor HAT Reader
    """

    name = "SensorHATReader"
    setting_prefix = "SENSOR_HAT_READER_"

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

        self.timezone = datetime.now(timezone(timedelta(0))).astimezone().tzinfo

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

    async def read(self) -> Dict[str, Union[Dict[str, float], datetime]]:
        """

        :return:
        :rtype: Dict[str, Union[Dict[str, float], datetime]]
        """
        timestamp = datetime.now(self.timezone)
        result = {
            k: v
            for pair in await asyncio.gather(
                self.get_humidity(),
                self.get_temperature_from_humidity(),
                self.get_pressure(),
                self.get_temperature_from_pressure(),
            )
            for k, v in pair.items()
        }
        return {
            "timestamp": timestamp,
            "result": result,
        }

    async def get_humidity(self) -> Dict[str, float]:
        """
        Gets the percentage of relative humidity from the humidity sensor.

        :return:
        :rtype: Dict[str, float]
        """
        return {"humidity": 0}

    async def get_temperature_from_humidity(self) -> Dict[str, float]:
        """
        Gets the current temperature in degrees Celsius from the humidity sensor.

        :return:
        :rtype: Dict[str, float]
        """
        return {"temperature_from_humidity": 0}

    async def get_pressure(self) -> Dict[str, float]:
        """
        Gets the current pressure in Millibars from the pressure sensor.

        :return:
        :rtype: Dict[str, Dict[str, float]
        """
        return {"pressure": 0}

    async def get_temperature_from_pressure(self) -> Dict[str, float]:
        """
        Gets the current temperature in degrees Celsius from the pressure sensor.

        :return:
        :rtype: Dict[str, float]
        """
        return {"temperature_from_pressure": 0}

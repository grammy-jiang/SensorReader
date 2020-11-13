"""
The signals used in Sensor Reader
"""
from sensor_reader.signals.manager import SignalManager


class Signal:
    def __init__(self, name: str):
        """

        :param name:
        :type name: str
        """
        self.name = name

    def __str__(self):
        """

        :return:
        """
        return self.name

    def __repr__(self):
        """

        :return:
        """
        return self.name


components_start = Signal("component_start")
components_stop = Signal("component_stop")

service_start = Signal("service_start")
service_stop = Signal("service_stop")

__all__ = [
    "Signal",
    "SignalManager",
    "components_start",
    "components_stop",
    "service_start",
    "service_stop",
]

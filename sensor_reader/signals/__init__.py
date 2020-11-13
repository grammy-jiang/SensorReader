"""
The signals used in Sensor Reader
"""
from sensor_reader.signals.manager import SignalManager

service_start = object()
service_stop = object()

__all__ = [
    "SignalManager",
    "service_start",
    "service_stop",
]

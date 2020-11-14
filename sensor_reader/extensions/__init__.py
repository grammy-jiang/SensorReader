"""
All ready to use extensions
"""

from sensor_reader.extensions.logstats import LogStats
from sensor_reader.extensions.manager import ExtensionManager
from sensor_reader.extensions.stats import Stats

__all__ = [
    "ExtensionManager",
    "LogStats",
    "Stats",
]

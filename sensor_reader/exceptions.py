"""
Exceptions
"""


class SensorReaderException(Exception):
    """
    The base exception
    """


class SettingsFrozenException(SensorReaderException):
    """
    The exception when modify a frozen settings instance
    """


class SettingsLowPriorityException(SensorReaderException):
    """
    The exception when modify a setting with a lower priority
    """

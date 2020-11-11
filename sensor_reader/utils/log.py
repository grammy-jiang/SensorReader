"""
Logging related utilities
"""

import logging
from functools import cached_property

from sensor_reader.settings import Settings


class LoggerMixin:  # pylint: disable=too-few-public-methods
    """
    Logger Mixin
    """

    @cached_property
    def logger(self) -> logging.Logger:
        """

        :return:
        :rtype: logging.Logger
        """
        name = ".".join(
            [
                self.__module__,
                self.__class__.__name__,
            ]
        )
        return logging.getLogger(name)


def configure_logging(settings: Settings) -> None:
    """

    :param settings:
    :type settings: Settings
    :return:
    :rtype: None
    """
    # Get a console handler and configure it
    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        fmt=settings["LOG_FORMATTER_FMT"],
        datefmt=settings["LOG_FORMATTER_DATEFMT"],
    )
    console_handler.setFormatter(formatter)
    console_handler.setLevel(settings["LOG_LEVEL"])

    # add this console handler into logging
    logging.root.addHandler(console_handler)

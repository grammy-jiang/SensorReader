"""
Entrypoint
"""
import logging
from argparse import Action, ArgumentParser, Namespace
from typing import Dict

import sensor_reader
from sensor_reader.settings import Settings
from sensor_reader.utils import configure_logging, get_runtime_info

logger = None  # pylint: disable=invalid-name


class SettingsAppend(Action):  # pylint: disable=too-few-public-methods
    """
    Save settings into dict
    """

    def __call__(
        self,
        parser: ArgumentParser,
        namespace: Namespace,
        values: str,
        option_string=None,
    ) -> None:
        """

        :param parser:
        :param namespace:
        :param values:
        :param option_string:
        :return:
        """
        items: Dict = getattr(namespace, self.dest)

        key: str
        value: str
        key, value = values.split("=", 1)
        items.update({key: value})

        setattr(namespace, self.dest, items)


def get_arguments(*args) -> Namespace:
    """

    :param args:
    :type args:
    :return:
    :rtype: Namespace
    """
    parser = ArgumentParser()

    parser.add_argument(
        "-s",
        "--settings",
        action=SettingsAppend,
        default=dict(),
        help="configure the setting from command line interface",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="print the version number and exit (also --version)",
        version=f"%(prog)s {sensor_reader.__version__}",
    )

    return parser.parse_args(args)


def set_logging(settings: Settings) -> None:
    """

    :param settings:
    :type settings: Settings
    :return:
    :rtype: None
    """
    configure_logging(settings)

    global logger  # pylint: disable=global-statement,invalid-name
    logger = logging.getLogger("sensor_reader")
    logger.setLevel(settings["LOG_LEVEL"])

    get_runtime_info()


def main():
    """

    :return:
    """

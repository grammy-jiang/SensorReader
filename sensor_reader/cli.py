"""
Entrypoint
"""
import logging
from argparse import Action, ArgumentParser, Namespace
from typing import Dict

import sensor_reader

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")


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


def main():
    """

    :return:
    """

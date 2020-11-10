"""
Test cases for sensor_reader.cli
"""
from argparse import Namespace
from unittest import TestCase

from sensor_reader.cli import get_arguments


class CLITest(TestCase):
    """
    Test cases for sensor_reader.cli
    """

    def test_get_arguments(self) -> None:
        """

        :return:
        :rtype: None
        """
        args = get_arguments("-s", "test_1=value", "--settings", "test_2=value")

        self.assertIsInstance(args, Namespace)
        self.assertIsInstance(args.settings, dict)
        self.assertDictEqual(args.settings, {"test_1": "value", "test_2": "value"})

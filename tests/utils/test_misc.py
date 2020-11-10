"""
Test cases for sensor_reader.utils.misc
"""
from unittest.case import TestCase

from sensor_reader.utils import load_object


class MiscTestCase(TestCase):
    """
    test functions in sensor_reader.utils.misc
    """

    def test_load_object(self) -> None:
        """

        :return:
        """
        obj = load_object("sensor_reader.utils.misc.load_object")
        self.assertIs(obj, load_object)

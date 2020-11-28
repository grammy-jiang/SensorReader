"""
Test cases for sensor_reader.utils.misc
"""
from unittest.case import TestCase

from sensor_reader.utils import load_object

tuple_ = tuple
test_tuple = ("a", "b")


class TestClass:
    def __init__(self, a, b, c=None, d=None):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    @classmethod
    def from_test_case(cls, a, b, c=None, d=None):
        obj = cls(a, b, c, d)
        return obj

    def __hash__(self):
        return hash(self.a) ^ hash(self.b) ^ hash(self.c) ^ hash(self.d)


class MiscTestCase(TestCase):
    """
    test functions in sensor_reader.utils.misc
    """

    def test_load_object(self) -> None:
        """

        :return:
        :rtype: None
        """
        obj = load_object("sensor_reader.utils.misc.load_object")
        self.assertIs(obj, load_object)

    def test_load_object_with_arguments(self) -> None:
        """

        :return:
        :rtype: None
        """
        obj = load_object("tests.utils.test_misc.tuple_", ("a", "b"))
        self.assertSequenceEqual(obj, ("a", "b"))

        obj = load_object(
            "tests.utils.test_misc.TestClass", 1, 2, init="from_test_case", c=3, d=4
        )
        self.assertEqual(hash(obj), hash(TestClass.from_test_case(1, 2, c=3, d=4)))

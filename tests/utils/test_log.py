"""
The test cases for sensor_reader.utils.log
"""
from typing import List, Tuple
from unittest import TestCase

from sensor_reader.utils.log import LoggerMixin


class TestClass(LoggerMixin):  # pylint: disable=too-few-public-methods
    """
    A test purpose class for LoggerMixin
    """

    name = "test_class"


class LoggerMixinTest(TestCase):
    """
    Test case for LoggerMixin
    """

    def setUp(self):
        """

        :return:
        """
        self.test_class = TestClass()

    def tearDown(self) -> None:
        """

        :return:
        """
        del self.test_class

    def test_logger_mixin(self):
        """

        :return:
        """
        self.assertTrue(hasattr(self.test_class, "logger"))

        messages: List[Tuple[str, str, Tuple]] = [
            ("info", "Hello %s!", ("test 0",)),
            ("error", "Hello %s!", ("test 1",)),
        ]
        with self.assertLogs(
            f"{self.__module__}.{self.test_class.__class__.__name__}",
            level="INFO",
        ) as cm_logs:
            for level, message, args in messages:
                getattr(self.test_class.logger, level)(message, *args)

        for (level, message, args), log_record in zip(messages, cm_logs.records):
            self.assertEqual(log_record.levelname, level.upper())
            self.assertEqual(log_record.msg, message)
            self.assertEqual(log_record.args, args)

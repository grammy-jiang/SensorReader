"""
The test cases for sensor_reader.utils.log
"""
import logging
from typing import List, Tuple
from unittest import TestCase
from unittest.mock import MagicMock, patch

from sensor_reader.settings import Settings
from sensor_reader.utils.log import LoggerMixin, configure_logging


class TestClass(LoggerMixin):  # pylint: disable=too-few-public-methods
    """
    A test purpose class for LoggerMixin
    """

    name = "test_class"


class LoggerMixinTest(TestCase):
    """
    Test case for LoggerMixin
    """

    def setUp(self) -> None:
        """

        :return:
        :rtype: None
        """
        self.test_class = TestClass()

    def tearDown(self) -> None:
        """

        :return:
        :rtype: None
        """
        del self.test_class

    def test_logger_mixin(self) -> None:
        """

        :return:
        :rtype: None
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


class FunctionsTest(TestCase):
    """
    the test cases for functions
    """

    @patch("logging.root")
    def test_configure_logging(self, root: MagicMock):
        """

        :param root:
        :type root: MagicMock
        :return:
        """
        settings = Settings(
            {
                "LOG_LEVEL": logging.INFO,
                "LOG_FORMATTER_FMT": "%(asctime)s [%(name)s] %(levelname)s: %(message)s",
                "LOG_FORMATTER_DATEFMT": "%Y-%m-%d %H:%M:%S",
            }
        )
        configure_logging(settings)

        root.addHandler.assert_called()

        call_args = root.addHandler.call_args_list
        handler: logging.StreamHandler = call_args[0].args[0]

        self.assertEqual(handler.level, logging.INFO)
        self.assertEqual(handler.formatter.datefmt, "%Y-%m-%d %H:%M:%S")  # type: ignore
        self.assertEqual(
            handler.formatter._fmt,  # pylint: disable=protected-access
            "%(asctime)s [%(name)s] %(levelname)s: %(message)s",
        )

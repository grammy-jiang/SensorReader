"""
Test BaseSettings class
"""

from collections.abc import Iterable
from unittest.case import TestCase

from sensor_reader.exceptions import (
    SettingsFrozenException,
    SettingsLowPriorityException,
)
from sensor_reader.settings import BaseSettings, Setting


class BaseSettingsTest(TestCase):
    """
    test BaseSettings class
    """

    def test_init(self) -> None:
        """
        test the initialize method
        :return:
        :rtype: None
        """

        settings = BaseSettings()
        self.assertDictEqual(settings._data, {})  # pylint: disable = protected-access

        settings = BaseSettings(settings={"a": 1, "b": 2})
        self.assertDictEqual(
            settings._data,  # pylint: disable = protected-access
            {
                "a": Setting(priority="project", priority_value=20, value=1),
                "b": Setting(priority="project", priority_value=20, value=2),
            },
        )

        self.assertTrue(settings.is_frozen())
        self.assertEqual(
            settings._priority, "project"  # pylint: disable = protected-access
        )

    def test_is_frozen(self) -> None:
        """
        test the method is_frozen
        :return:
        :rtype: None
        """

        settings = BaseSettings()
        self.assertTrue(settings.is_frozen())

        with settings.unfreeze() as settings_:
            self.assertFalse(settings_.is_frozen())

    def test_unfreeze(self) -> None:
        """
        test the context manager unfreeze
        :return:
        :rtype: None
        """

        settings = BaseSettings()
        self.assertTrue(settings.is_frozen())
        with settings.unfreeze() as settings_:
            self.assertFalse(settings_.is_frozen())
        self.assertEqual(
            settings._priority,  # pylint: disable = protected-access
            "project",
        )

        with settings.unfreeze(priority="user") as settings_:
            self.assertFalse(settings_.is_frozen())
            self.assertEqual(
                settings_._priority, "user"  # pylint: disable = protected-access
            )
        self.assertEqual(
            settings._priority, "project"  # pylint: disable = protected-access
        )

    def test_setitem(self):
        """
        test the method of setitem
        :return:
        """
        settings = BaseSettings(settings={"a": 1, "b": 2})
        with settings.unfreeze() as settings_:
            settings_["c"] = 3
        self.assertEqual(settings["c"], 3)

        with self.assertRaises(SettingsFrozenException):
            settings["c"] = 3

        with self.assertRaises(SettingsLowPriorityException):
            with settings.unfreeze("default") as settings_:
                settings_["a"] = 3

    def test_delitem(self):
        """
        test the method of del
        :return:
        """
        settings = BaseSettings(settings={"a": 1, "b": 2})
        with settings.unfreeze() as settings_:
            del settings_["a"]
        self.assertNotIn("a", settings)

        with self.assertRaises(SettingsFrozenException):
            del settings["a"]

    def test_getitem(self):
        """
        test the method of getitem
        :return:
        """
        settings = BaseSettings(settings={"a": 1, "b": 2})
        self.assertEqual(settings["a"], 1)

    def test_len(self):
        """
        test the method of len
        :return:
        """
        settings = BaseSettings(settings={"a": 1, "b": 2})
        self.assertEqual(len(settings), 2)

        settings = BaseSettings()
        self.assertEqual(len(settings), 0)

    def test_iter(self):
        """
        test the method of iter
        :return:
        """
        settings = BaseSettings()
        self.assertIsInstance(settings, Iterable)

    def test_contains(self):
        """
        test the method of contains
        :return:
        """
        settings = BaseSettings(settings={"a": 1, "b": 2})
        self.assertTrue("a" in settings)
        self.assertFalse("c" in settings)

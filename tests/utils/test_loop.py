"""
Test case for sensor_reader.utils.loop
"""

from asyncio.unix_events import SelectorEventLoop
from unittest import TestCase
from unittest.mock import MagicMock, patch

from sensor_reader.settings import Settings
from sensor_reader.utils import configure_event_loop


class LoopTest(TestCase):
    """
    Test case for sensor_reader.utils.loop
    """

    @patch("asyncio.set_event_loop")
    def test_loop(self, set_event_loop: MagicMock):
        """

        :return:
        """
        settings = Settings({"LOOP": "asyncio"})

        configure_event_loop(settings)

        set_event_loop.assert_called()

        loop = set_event_loop.call_args_list[0].args[0]

        self.assertIsInstance(loop, SelectorEventLoop)

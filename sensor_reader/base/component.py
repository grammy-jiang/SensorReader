"""
Base Class for Components
"""
from typing import Any, Dict, Optional

from sensor_reader.signals import Signal, components_start, components_stop
from sensor_reader.utils import LoggerMixin


class BaseComponent(LoggerMixin):
    """
    Base Class for Components, including:
    * manager
    * middleware
    * extension
    * channel
    """

    name: Optional[str] = None
    setting_prefix: str = ""

    def __init__(self, service, name: str = None, setting_prefix: str = None):
        """

        :param service:
        :type service:
        :param name:
        :type name: str
        :param setting_prefix
        :type setting_prefix: str
        """
        self.service = service
        self.settings = service.settings

        if name:
            self.name = name

        if setting_prefix:
            self.setting_prefix = setting_prefix

        self.config: Dict[str, Any] = {
            key.replace(self.setting_prefix, ""): value
            for key, value in self.settings.items()
            if key.startswith(self.setting_prefix)
        }

    @classmethod
    def from_service(cls, service, name: str = None, setting_prefix: str = None):
        """
        Initialize components from a service instance
        :param service:
        :type service:
        :param name:
        :type name: str
        :param setting_prefix:
        :type setting_prefix: str
        :return:
        """
        obj = cls(service, name, setting_prefix)

        signal_manager = service.signal_manager

        signal_manager.connect(obj.start, components_start)
        signal_manager.connect(obj.stop, components_stop)

        return obj

    async def start(self, signal: Signal, sender) -> None:
        """

        :param signal:
        :type signal: Signal
        :param sender:
        :return:
        :rtype: None
        """

    async def stop(self, signal: Signal, sender) -> None:
        """

        :param signal:
        :type signal: Signal
        :param sender:
        :return:
        :rtype: None
        """

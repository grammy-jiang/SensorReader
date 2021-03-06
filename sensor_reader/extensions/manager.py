"""
Extension Manager
"""
import pprint
from functools import cached_property
from typing import Dict

from sensor_reader.base import BaseComponent, ManagerMixin


class ExtensionManager(ManagerMixin, BaseComponent):
    """
    Extension Manager
    """

    manage = "EXTENSIONS"
    name = "ExtensionManager"
    setting_prefix = "EXTENSION_MANAGER_"

    def __init__(self, service, name: str = None, setting_prefix: str = None):
        """

        :param service:
        :type service:
        :param name:
        :type name: str
        :param setting_prefix:
        :type setting_prefix:
        """
        super().__init__(service, name, setting_prefix)

        self._initialize_components()

        self.logger.info(
            "Enabled extensions:\n%s", pprint.pformat(self.cls_extensions)
        )

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

        return obj

    @cached_property
    def cls_extensions(self) -> Dict[str, int]:
        """
        Get all extensions with the priority in a dict
        :return:
        :rtype: Dict[str, int]
        """
        return self._cls_components

    @cached_property
    def extensions(self) -> Dict[str, object]:
        """
        Get all extensions by names in a dict
        :return:
        :rtype: Dict[str, object]
        """
        return self._components

    def get_extension(self, name: str) -> object:
        """
        Get an extension by its name
        :param name:
        :type name: str
        :return:
        :rtype: object
        """
        return self.extensions[name]

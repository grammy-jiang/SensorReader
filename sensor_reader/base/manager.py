"""
Base Manager Class for extensions and middlewares
"""
from functools import cached_property
from typing import Dict

from sensor_reader.settings import Settings
from sensor_reader.utils import load_object

from .service import BaseService


class ManagerMixin:  # pylint: disable=too-few-public-methods
    """
    Base Manager Class for extensions and middlewares
    """

    manage: str
    settings: Settings
    service: BaseService
    _components_: Dict[str, object]

    @cached_property
    def _cls_components(self) -> Dict[str, int]:
        """

        :return:
        :rtype: Dict[str, int]
        """
        return dict(
            sorted(
                self.settings[self.manage].items(),
                key=lambda items: items[1],
            )
        )

    def _initialize_components(self) -> None:
        """

        :return:
        :rtype: None
        """
        self._components_: Dict[str, object] = {
            cls.__name__: cls.from_service(self.service)
            for cls in (load_object(cls) for cls in self._cls_components.keys())
        }

    @cached_property
    def _components(self) -> Dict[str, object]:
        """

        :return:
        :rtype: Dict[str, object]
        """
        if not self._components_:
            self._initialize_components()
        return self._components_

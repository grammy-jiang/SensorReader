"""
Base Manager Class for extensions and middlewares
"""
from functools import cached_property
from typing import Dict, Optional

from sensor_reader.settings import Settings
from sensor_reader.utils import load_object

from .service import BaseService


class ManagerMixin:  # pylint: disable=too-few-public-methods
    """
    Base Manager Class for extensions and middlewares
    """

    manage: Optional[str] = None
    settings: Settings
    service: BaseService

    @cached_property
    def _cls_components(self) -> Dict[str, int]:
        """

        :return:
        :rtype: Dict[str, int]
        """
        return dict(
            sorted(
                self.settings[self.manage].items(),  # type: ignore
                key=lambda items: items[1],
            )
        )

    @cached_property
    def _components(self) -> Dict[str, object]:
        """

        :return:
        :rtype: Dict[str, object]
        """
        return {
            cls.name: cls.from_service(self.service)  # type: ignore
            for cls in (load_object(cls) for cls in self._cls_components.keys())
        }

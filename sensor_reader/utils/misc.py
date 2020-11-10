"""
Miscellaneous functions
"""
from functools import lru_cache
from importlib import import_module
from types import ModuleType
from typing import Any


@lru_cache
def load_object(path: str) -> Any:
    """
    Load an object given its absolute object path, and return it.

    object can be the import path of a class, function, variable or an
    instance, e.g. "sensor_reader.service.sensor_reader"

    :param path:
    :type path: str
    :return:
    :rtype: Any
    """
    module: str
    name: str
    module, name = path.rsplit(".", 1)
    mod: ModuleType = import_module(module)

    return getattr(mod, name)

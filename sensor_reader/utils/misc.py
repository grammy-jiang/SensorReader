"""
Miscellaneous functions
"""
from functools import lru_cache
from importlib import import_module
from types import ModuleType
from typing import Any, Callable


@lru_cache
def load_object(path: str, *args, init: str = None, **kwargs) -> Any:
    """
    Load an object given its absolute object path, and return it.

    object can be the import path of a class, function, variable or an instance,
    e.g. "functools.lru_cache"

    :param path:
    :type path: str
    :param args:
    :type args:
    :param init:
    :type init: str
    :param kwargs:
    :type kwargs:
    :return:
    :rtype: Any
    """
    module: str
    name: str
    module, name = path.rsplit(".", 1)
    mod: ModuleType = import_module(module)

    type_ = getattr(mod, name)

    type_init: Callable = getattr(type_, init) if init else type_

    if args or kwargs:
        return type_init(*args, **kwargs)
    else:
        return type_init

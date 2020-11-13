"""
Create a singleton object for asyncio loop
"""
import asyncio

from sensor_reader.settings import Settings

from .misc import load_object


def configure_event_loop(
    settings: Settings, func: str = "new_event_loop", **kwargs
) -> None:
    """
    configure event loop; currently only support asyncio and uvloop

    :param settings:
    :type settings: Settings
    :param func:
    :type func: str
    :param kwargs:
    :return:
    :rtype: AbstractEventLoop
    """

    loop_path: str = ".".join([settings.get("LOOP", "asyncio"), func])
    loop = load_object(loop_path)(**kwargs)
    asyncio.set_event_loop(loop)

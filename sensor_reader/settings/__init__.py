"""
Settings
"""

from collections import namedtuple
from typing import Dict

# The pair of priority and priority_value
PRIORITIES: Dict[str, int] = {
    "default": 0,
    "project": 20,
    "env": 40,
    "cmd": 60,
}

Setting = namedtuple("Setting", ["priority", "priority_value", "value"])

"""
Settings
"""

from typing import Dict

# The pair of priority and priority_value
PRIORITIES: Dict[str, int] = {
    "default": 0,
    "project": 20,
    "env": 40,
    "cmd": 60,
}

"""
Default settings
"""

import logging

# ==== LOG CONFIGURATION ======================================================

LOG_LEVEL = logging.INFO
LOG_FORMATTER_FMT = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
LOG_FORMATTER_DATEFMT = "%Y-%m-%d %H:%M:%S"

# ==== CORE MODULES ===========================================================

LOOP = "uvloop"

CLS_SERVICE = "sensor_reader.services.SensorReader"

CLS_SIGNAL_MANAGER = "sensor_reader.signals.SignalManager"

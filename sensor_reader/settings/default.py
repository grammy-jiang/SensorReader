"""
Default settings
"""

import logging
from typing import Dict

# ==== LOG CONFIGURATION ======================================================

LOG_LEVEL = logging.INFO
LOG_FORMATTER_FMT = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
LOG_FORMATTER_DATEFMT = "%Y-%m-%d %H:%M:%S"

# ==== CORE MODULES ===========================================================

LOOP = "uvloop"

CLS_SERVICE = "sensor_reader.services.SensorReaderService"

CLS_SIGNAL_MANAGER = "sensor_reader.signals.SignalManager"

CLS_EXTENSION_MANAGER = "sensor_reader.extensions.ExtensionManager"

CLS_CHANNEL_MANAGER = "sensor_reader.channels.ChannelManager"

# ==== Extensions =============================================================

EXTENSIONS: Dict[str, int] = {
    "sensor_reader.extensions.LogStats": 0,
    "sensor_reader.extensions.Stats": 0,
}

LOGSTATS_INTERVAL = 60  # in seconds

CHANNELS: Dict[str, Dict] = {
    "sense_hat": {
        "readers": [
            "sensor_reader.readers.SensorHATReader",
        ],
        "pipelines": [
            "sensor_reader.pipelines.PostgreSQLPipeline",
        ],
    },
}

CHANNELS_MANAGER_CHANNEL_SENSE_HAT_SCHEDULE: Dict[str, str] = {
    "second": "*",
}

postgres_user = "user"
postgres_password = "password"
postgres_host = "host"
postgres_port = "post"
postgres_database = "db"
POSTGRESQL_PIPELINE_POSTGRESQL_URL = (
    f"postgres://"
    f"{postgres_user}:{postgres_password}@"
    f"{postgres_host}:{postgres_port}/"
    f"{postgres_database}"
)

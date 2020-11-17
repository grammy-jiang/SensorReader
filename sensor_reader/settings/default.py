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
            "sensor_reader.pipelines.MongoDBPipeline",
            "sensor_reader.pipelines.PostgreSQLPipeline",
            "sensor_reader.pipelines.LocalFilePipeline",
        ],
    },
}

CHANNELS_MANAGER_CHANNEL_SENSE_HAT_SCHEDULE: Dict[str, str] = {
    "second": "*",
}

POSTGRESQL_PIPELINE_POSTGRES_USER = "sense-hat"
POSTGRESQL_PIPELINE_POSTGRES_PASSWORD = "password"
POSTGRESQL_PIPELINE_POSTGRES_HOST = "192.168.1.115"
POSTGRESQL_PIPELINE_POSTGRES_PORT = 55432
POSTGRESQL_PIPELINE_POSTGRES_DATABASE = "sense-hat"
POSTGRESQL_PIPELINE_POSTGRESQL_URL = (
    f"postgres://"
    f"{POSTGRESQL_PIPELINE_POSTGRES_USER}:{POSTGRESQL_PIPELINE_POSTGRES_PASSWORD}@"
    f"{POSTGRESQL_PIPELINE_POSTGRES_HOST}:{POSTGRESQL_PIPELINE_POSTGRES_PORT}/"
    f"{POSTGRESQL_PIPELINE_POSTGRES_DATABASE}"
)

LOCAL_FILE_PIPELINE_FILE = "sense-hat_records.txt"

MONGODB_PIPELINE_MONGODB_USER = "sense-hat"
MONGODB_PIPELINE_MONGODB_PASSWORD = "password"
MONGODB_PIPELINE_MONGODB_HOST = "192.168.1.115"
MONGODB_PIPELINE_MONGODB_PORT = 27017
MONGODB_PIPELINE_MONGODB_DATABASE = "sense-hat"
MONGODB_PIPELINE_MONGODB_URL = (
    f"mongodb://"
    f"{MONGODB_PIPELINE_MONGODB_USER}:{MONGODB_PIPELINE_MONGODB_PASSWORD}@"
    f"{MONGODB_PIPELINE_MONGODB_HOST}:{MONGODB_PIPELINE_MONGODB_PORT}/"
    f"{MONGODB_PIPELINE_MONGODB_DATABASE}"
)

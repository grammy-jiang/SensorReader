"""
Pipelines
"""

from sensor_reader.pipelines.local_file import LocalFilePipeline
from sensor_reader.pipelines.mongodb import MongoDBPipeline
from sensor_reader.pipelines.postgresql import PostgreSQLPipeline

__all__ = [
    "LocalFilePipeline",
    "MongoDBPipeline",
    "PostgreSQLPipeline",
]

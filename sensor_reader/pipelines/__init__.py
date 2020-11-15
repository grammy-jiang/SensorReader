"""
Pipelines
"""

from sensor_reader.pipelines.local_fiel import LocalFilePipeline
from sensor_reader.pipelines.postgresql import PostgreSQLPipeline

__all__ = [
    "LocalFilePipeline",
    "PostgreSQLPipeline",
]

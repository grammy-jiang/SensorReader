"""
Pipeline of saving data to PostgreSQL
"""
import asyncpg
from asyncpg.pool import Pool, PoolConnectionProxy

from sensor_reader.base import BaseComponent
from sensor_reader.signals import Signal


class PostgreSQLPipeline(BaseComponent):
    """
    Pipeline of saving data to PostgreSQL
    """

    name = "PostgreSQLPipeline"
    setting_prefix = "POSTGRESQL_PIPELINE_"

    pg_pool: Pool

    async def start(self, signal: Signal, sender) -> None:
        """

        :param signal:
        :type signal: Signal
        :param sender:
        :type sender:
        :return:
        :rtype: None
        """
        self.pg_pool: Pool = await asyncpg.create_pool(self.config["POSTGRESQL_URL"])

        conn: PoolConnectionProxy
        async with self.pg_pool.acquire() as conn:
            version: str = await conn.fetchval("SELECT version()")

            self.logger.info(
                "PostgreSQL [%s:%s] is connected:\n%s", *conn._con._addr, version
            )

    async def process_item(self, item) -> None:
        """

        :param item:
        :return:
        """
        # TODO: receive value and save to database

    async def stop(self, signal: Signal, sender) -> None:
        """

        :param signal:
        :type signal: Signal
        :param sender:
        :return:
        :rtype: None
        """
        self.logger.info("PostgreSQL is disconnected")
        await self.pg_pool.close()

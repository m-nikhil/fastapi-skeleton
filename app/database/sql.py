import databases

from ..utils.singletonMeta import SingletonMeta


# Driver support is providing using one of asyncpg, aiomysql, or aiosqlite.
class Database(metaclass=SingletonMeta):

    _database: databases.Database = None

    def __init__(
        self,
        pg_user,
        pg_password,
        pg_host,
        pg_port,
        pg_database,
        max_pool_size,
        min_pool_size,
    ):
        connection_string = (
            f"postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_database}"
        )
        self._database = databases.Database(
            connection_string, min_size=min_pool_size, max_size=max_pool_size
        )

    async def connect(self):
        await self._database.connect()

    async def disconnect(self):
        await self._database.disconnect()

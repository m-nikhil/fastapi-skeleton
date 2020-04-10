import databases

from ..utils.singletonMeta import SingletonMeta


class Database(metaclass=SingletonMeta):

    def __init__(self, connection_string):
        self._connectionString = connection_string
        self._database = databases.Database(self._connectionString)

    async def connect(self):
        await self._database.connect()

    async def disconnect(self):
        await self._database.disconnect()

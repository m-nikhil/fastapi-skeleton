from motor.motor_asyncio import AsyncIOMotorClient

from ..utils.singletonMeta import SingletonMeta


class Database(metaclass=SingletonMeta):

    _client: AsyncIOMotorClient = None

    def __init__(self, connectionString, maxPoolSize, minPoolSize):
        self._connectionString = connectionString
        self._maxPoolSize = maxPoolSize
        self._minPoolSize = minPoolSize

    async def connect(self):
        self._client = AsyncIOMotorClient(
            str(self._connectionString),
            maxPoolSize=self._maxPoolSize,
            minPoolSize=self._minPoolSize,
        )

    async def disconnect(self):
        self._client.close()

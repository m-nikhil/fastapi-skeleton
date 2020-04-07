from pydantic import BaseModel, BaseSettings

class DatabaseConfig():
    connection_string: str = 'mongodb://localhost:27017/'
    max_pool_size: int = 100
    min_pool_size: int = 10

class Configs(BaseSettings):
    database: DatabaseConfig = DatabaseConfig()
    project_name: str

    class Config:
        env_file = ".env"

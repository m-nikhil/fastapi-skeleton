from pydantic import BaseSettings


class DatabaseConfig():
    connection_string = "postgresql://postgres:database@localhost:5432/db"


class Configs(BaseSettings):
    database: DatabaseConfig = DatabaseConfig()
    project_name: str

    class Config:
        env_file = ".env"

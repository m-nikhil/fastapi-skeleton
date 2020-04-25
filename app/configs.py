from pydantic import BaseModel, BaseSettings

class Configs(BaseSettings):

    # Database config
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: str
    postgres_db: str
    max_pool_size: int = 100
    min_pool_size: int = 10

    project_name: str

    class Config:
        env_file = ".env"

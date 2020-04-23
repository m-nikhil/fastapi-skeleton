from pydantic import BaseModel, BaseSettings

class Configs(BaseSettings):

    # Database config
    connection_string: str
    max_pool_size: int = 100
    min_pool_size: int = 10

    project_name: str

    class Config:
        env_file = ".env"

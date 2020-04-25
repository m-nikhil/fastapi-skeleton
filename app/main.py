from fastapi import FastAPI

from .api.v1.router import router
from .configs import Configs
from .database.sql import Database

configs = Configs()
db = Database(configs.postgres_user,
                configs.postgres_password,
                configs.postgres_host,
                configs.postgres_port,
                configs.postgres_db,
                configs.max_pool_size, 
                configs.min_pool_size)

app = FastAPI(title=configs.project_name)

app.add_event_handler("startup", db.connect)
app.add_event_handler("shutdown", db.disconnect)

app.include_router(router, prefix='/v1')
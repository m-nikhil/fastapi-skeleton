from fastapi import FastAPI

from .api.v1.router import router
from .configs import Configs
from .database.mongo import Database

configs = Configs()
db = Database(configs.database.connection_string, 
                configs.database.max_pool_size, 
                configs.database.min_pool_size)

app = FastAPI(title=configs.project_name)

app.add_event_handler("startup", db.connect)
app.add_event_handler("shutdown", db.disconnect)

app.include_router(router, prefix='/v1')
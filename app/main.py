from fastapi import FastAPI

from .api.v1.router import router
from .configs import Configs

configs = Configs()

app = FastAPI()

app.include_router(router, prefix='/v1')
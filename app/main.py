import logging
import time

from fastapi import FastAPI
from fastapi import Request

from .api.v1.router import router
from .configs import Configs
from .database.sql import Database
from .logConfig import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)
configs = Configs()
db = Database(
    configs.postgres_user,
    configs.postgres_password,
    configs.postgres_host,
    configs.postgres_port,
    configs.postgres_db,
    configs.max_pool_size,
    configs.min_pool_size,
)

app = FastAPI(title=configs.project_name)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    logger.debug(
        "Request %s:%d '%s %s'",
        request.client.host,
        request.client.port,
        request.method,
        request.url.path,
    )
    start_time = time.time()
    response = await call_next(request)
    process_time = round((time.time() - start_time) * 1000, 2)
    logger.debug(
        "Response %s:%d '%s %s' %d (process_time: %.2f ms)",
        request.client.host,
        request.client.port,
        request.method,
        request.url.path,
        response.status_code,
        process_time,
    )
    return response


app.add_event_handler("startup", db.connect)
app.add_event_handler("shutdown", db.disconnect)

app.include_router(router, prefix="/v1")
logger.info("Server has started running")

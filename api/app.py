from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.v1.check_imei.routes import router as check_imei_router


@asynccontextmanager
async def lifespan(_: FastAPI):

    yield

app = FastAPI(lifespan=lifespan)


app.include_router(
    check_imei_router,
)
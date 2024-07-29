from pathlib import Path
from contextlib import asynccontextmanager

from fastapi import FastAPI
from helpers.router import DirRouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
router = DirRouter(Path(__file__).parent.joinpath("app"))  # ./app directory

app.include_router(router)

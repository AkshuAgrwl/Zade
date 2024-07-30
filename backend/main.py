import os
from pathlib import Path

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from supertokens_python.recipe import emailpassword, dashboard
from supertokens_python.framework.fastapi import get_middleware
from supertokens_python import (
    init as st_init,
    InputAppInfo,
    SupertokensConfig,
    get_all_cors_headers,
)

from helpers.router import DirRouter


app = FastAPI()

router = DirRouter(Path(__file__).parent.joinpath("app"))  # ./app directory
app.include_router(router)

st_init(
    app_info=InputAppInfo(
        app_name=os.environ["APP_NAME"],
        api_domain="http://localhost:8000",
        api_base_path="/auth/",
        website_domain=os.environ["SITE_URL"],
        website_base_path="/auth",
    ),
    supertokens_config=SupertokensConfig(
        connection_uri=os.environ["SUPERTOKENS_CONNECTION_URI"]
    ),
    framework="fastapi",
    recipe_list=[
        emailpassword.init(),
        dashboard.init(),
    ],
    mode="asgi",
)

app.add_middleware(get_middleware())
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ["SITE_URL"]],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD", "TRACE"],
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)

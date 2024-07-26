import os
import click
import asyncio

from hypercorn.asyncio import serve  # type:ignore
from hypercorn.config import Config

from app.main import app


@click.command()
@click.option(
    "--env",
    type=click.Choice(["dev", "prod"], case_sensitive=False),
    default=None,
    help=(
        "Sets the environment to run the server in."
        " This setting can also be enabled by setting the value of 'FASTAPI_ENV' environment variable."
        " Note that this option has the precedence over FASTAPI_ENV variable."
    ),
)
def main(env: str | None = None):
    debug: bool = False

    if env is None:
        FASTAPI_ENV = os.getenv("FASTAPI_ENV")
        if FASTAPI_ENV and FASTAPI_ENV.lower() in ["dev", "development"]:
            env = "dev"

    config = Config()
    config.bind = ["0.0.0.0:8000"]

    if env == "dev":
        config.use_reloader = True
        debug = True

    asyncio.run(
        serve(
            app,  # type: ignore
            config,
        ),
        debug=debug,
    )


if __name__ == "__main__":
    main()

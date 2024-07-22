FROM python:3.12.4-slim-bullseye

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VERSION=1.8.3 \
    POETRY_NO_INTERACTION=1 \
    POETRY_NO_ANSI=1 \
    VENV_PATH=/backend/.venv
ENV PATH="$POETRY_HOME/bin:${VENV_PATH}/bin:$PATH"

RUN apt-get update -qq && apt-get install --no-install-recommends -y curl build-essential
RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /backend

COPY poetry.lock* poetry.toml pyproject.toml ./
RUN poetry install

COPY ./app ./app

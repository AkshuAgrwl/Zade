FROM node:22.5.1-bullseye-slim

WORKDIR /frontend

RUN apt-get update -qq && apt-get install --no-install-recommends -y curl

COPY package.json package-lock.json* ./
RUN \
    if [ -f package-lock.json ]; then npm ci; \
    else echo "Warning: Lockfile not found. It is recommended to commit lockfiles to version control." && npm install; \
    fi

COPY . .

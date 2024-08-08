FROM node:22.5.1-bullseye-slim

WORKDIR /frontend

RUN apt-get update -qq && apt-get install --no-install-recommends -y curl

COPY package.json package-lock.json* ./
RUN \
    if [ -f package-lock.json ]; then npm ci; \
    else echo "Warning: Lockfile not found. It is recommended to commit lockfiles to version control." && npm install; \
    fi

ARG NEXT_PUBLIC_APP_NAME
ENV NEXT_PUBLIC_APP_NAME ${NEXT_PUBLIC_APP_NAME}
ARG NEXT_PUBLIC_API_URI
ENV NEXT_PUBLIC_API_URI ${NEXT_PUBLIC_API_URI}
ARG NEXT_PUBLIC_API_AUTH_BASE_PATH
ENV NEXT_PUBLIC_API_AUTH_BASE_PATH ${NEXT_PUBLIC_API_AUTH_BASE_PATH}
ARG NEXT_PUBLIC_SITE_URL
ENV NEXT_PUBLIC_SITE_URL ${NEXT_PUBLIC_SITE_URL}

COPY . .

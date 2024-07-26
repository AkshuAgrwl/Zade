# Zade
A Music Streaming Service!

## Requirements
- Docker 4.30 or above

## Development Setup
- Git clone the repository
    
    ```sh
    git clone https://github.com/AkshuAgrwl/Zade
    cd Zade
    ```

- Rename [`.env.example`](./.env.example) to `.env`.

- Fill the credentials/parameters in the `.env` file accordingly. (Check [Environment Variables](#environment-variables) section)

- Generate the image and run the docker container (in development environment)
    ```sh
    docker compose -f docker-compose.yaml -f docker-compose.dev.yaml up --watch
    ```

#### **Note**: To enable type-checking and other features in your IDE, you need to install the packages locally.

- Before running the docker compose, install the packages locally by following the below steps.

- Install [Backend](./backend/) packages:

    ```sh
    cd backend
    poetry install
    ```

- Install [Frontend](./frontend/) fackages:

    ```sh
    cd frontend
    npm install
    ```

## Environment Variables

- `ENVIRONMENT`: The environment the project is running in. (`development`/`production`).

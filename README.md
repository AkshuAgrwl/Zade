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

- Generate the image and run the docker container
    - In development environment:
        
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

> **Note:** Some general variables may be pre-defined in [`.env.example`](./.env.example) which can be left unchanged if you want to run the project in development. But they must be changed (or verified) in production.

> Some parameters like passwords and secret keys must be set before running the project. For generating secret keys, follow the guide in [Environment Variables](#environment-variables) section.


#### General:

- `ENVIRONMENT`: The environment the project is running in. (`development`/`production`).

#### Frontend:

- `FRONTEND_NEXTJS_PORT`: Port to expose the frontend Next.js server on. (Default: `3000`)

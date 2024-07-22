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

- Rename [`.env.development.example`](./.env.development.example) to `.env.development`.

- Fill the credentials/parameters in the `.env.development` file accordingly. (Check [Environment Variables](#environment-variables) section)

- Generate the image and run the docker container
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

- `NEXT_TELEMETRY_DISABLED`: Next.js collects completely anonymous telemetry data about general usage. Learn more here: https://nextjs.org/telemetry. (`true`/`false`)

#### Pre-defined variables (not recommended to modify):

- `ENVIRONMENT`: The environment the project is running in. (`development`/`production`).

- `NODE_ENV`: Node.js environment. (`development`/`production`).

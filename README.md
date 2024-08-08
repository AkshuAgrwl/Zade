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

- `APP_NAME`: Name of the Application. (Default: `Zade`)

- `SITE_URL`: The public URL of the site. (Default: `http://localhost:3000`)

#### Frontend:

- `FRONTEND_NEXTJS_PORT`: Port to expose the frontend Next.js server on. (Default: `3000`)

#### Backend:

- `BACKEND_FASTAPI_PORT`: Port to expose the backend FastAPI server on. (Default: `8000`)

#### Database:

- `POSTGRES_USER`: Postgres default user.

- `POSTGRES_PASSWORD`: Password for the `POSTGRES_USER`.

- `POSTGRES_DB`: Default postgres database.

#### SuperTokens:

- `SUPERTOKENS_POSTGRES_USER`: Postgres user for supertokens. This will be created during database initialization with ownership to the `SUPABASE_POSTGRES_DB` database.

- `SUPERTOKENS_POSTGRES_PASSWORD`: Password for the `SUPERTOKENS_POSTGRES_USER`.

- `SUPERTOKENS_POSTGRES_DB`: Database for SuperTokens. This will be created during initialization and it's ownership will be given to `SUPERTOKENS_POSTGRES_USER`.

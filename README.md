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

    > Note: To run supabase storage service with S3, check out [Running Supabase Storage with S3 Backend](#running-supabase-storage-with-s3-backend).

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

## Running Supabase Storage with S3 Backend

- Set the values of environment variables for S3 backend:

    ```sh
    SUPABASE_STORAGE_S3_GLOBAL_S3_BUCKET=name-of-your-s3-bucket
    SUPABASE_STORAGE_S3_REGION=region-of-your-s3-bucket
    ```

- Run the docker container by including [`docker-compose.s3.yaml`](./docker-compose.s3.yaml) using the `-f` flag in the docker compose command.

## Environment Variables

> **Note:** Some general variables have been pre-defined in [`.env.example`](./.env.example) which can be left unchanged if you want to run the project in development. But they must be changed (or verified) in production.

> Some parameters like passwords and secret keys must be set before running the project. For generating secret keys, follow the guide in [Environment Variables](#environment-variables) section.

> Some optional parameters depends on the features enabled. For example, `SUPABASE_STORAGE_S3_GLOBAL_S3_BUCKET` and `SUPABASE_STORAGE_S3_REGION` are required to be set only when the Supabase Storage S3 backend is enabled.

#### General:

- `ENVIRONMENT`: The environment the project is running in. (`development`/`production`).

#### Frontend:

- `FRONTEND_NEXTJS_PORT`: Port to expose the frontend Next.js server on. (Default: `3000`)

#### Database:

- `POSTGRES_PASSWORD`: Password for the postgres server.

- `POSTGRES_DB`: Name of the postgres database.

- `POSTGRES_PORT`: Port to run the postgres server on.

#### Supabase:

> Follow the [Supabase's Self Hosting with Docker Guide](https://supabase.com/docs/guides/self-hosting/docker) to understand and configure the environment variables. Note that most of the variables already provided by the supabase have been modified (mostly prefixed with `SUPABASE_` or `SUPABASE_<service_name>_`). Some important variables are explained below:

- `SUPABASE_JWT_SECRET`: A JWT Secret key for Supabase. Generate a JWT secret and use it. Make sure to keep it safe and not push it in version control.

- `SUPABASE_ANON_KEY`: A low privileged secret key. You can generate it using your JWT secret from [Supabase's API Keys Generator](https://supabase.com/docs/guides/self-hosting/docker#generate-api-keys). Read more about it [here](https://supabase.com/docs/guides/api/api-keys#the-anon-key).

- `SUPABASE_SERVICE_ROLE_KEY`: A secret key set for a predefined Postgres Role to run various jobs in backend. You can generate it using your JWT secret from [Supabase's API Keys Generator](https://supabase.com/docs/guides/self-hosting/docker#generate-api-keys). Do not expose it anywhere in a publically available environment. Read more about it [here](https://supabase.com/docs/guides/api/api-keys#the-servicerole-key).

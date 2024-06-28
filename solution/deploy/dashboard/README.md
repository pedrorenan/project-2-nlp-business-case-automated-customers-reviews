# Dashboard Deployment

This dasboard was created using Evidence. See more about Evidence [here](https://.evidence.dev)

## Pre-requisites

- Postgres Database - You can use the seed.sql file to create the tables and load the data

## How to run

1. Clone the repository
2. Create a connection.options.yaml file in sources/project/ with the following content
```yaml
    user: base64 encoded your posgres database user
    password: base64 encoded your posgres database password
    ssl: {}
```
3. If necessary, change host, port or database in sources/project/connection.yaml
4. Run the following command to install the dependencies
```bash
npm install
```
5. Run the following command to start the application
```bash
npm run dev
```
6. Open your browser and go to http://localhost:3000
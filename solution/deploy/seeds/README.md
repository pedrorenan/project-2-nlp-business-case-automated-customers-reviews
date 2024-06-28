# Seed script to populate the database with initial data

This script will get the data from the CSV files and insert it into the database.

## Pre-requisites

- A CSV file with the data to be inserted into the database
- Postgres Database

## How to run

1. Clone the repository
2. Create a `.env` file with the following content:

```bash
cp .env.example .env
```

3. Update the `.env` file with the database connection string
4. Run the following command to install the dependencies

```bash
pip install -r requirements.txt
```

5. Run the following command to run the script

```bash
python app.py
```


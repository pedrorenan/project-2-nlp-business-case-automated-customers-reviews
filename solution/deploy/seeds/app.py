from sqlalchemy import create_engine, Table, Column, Integer, Float, String, MetaData
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the database URL from the environment variables
database_url = os.getenv("DATABASE_URL")

# Create a connection to the database using SQLAlchemy
engine = create_engine(database_url)

# Read a CSV file containing data into a pandas DataFrame
df = pd.read_csv('dataset_with_summaries.csv')

# Create a MetaData object which will be used to store schema information of the database
metadata = MetaData()

def infer_sqlalchemy_type(dtype):
    """ 
    Map pandas dtype to SQLAlchemy's types 
    """
    if "int" in dtype.name:
        return Integer
    elif "float" in dtype.name:
        return Float
    elif "object" in dtype.name:
        return String
    else:
        return String

# Create a list of SQLAlchemy Column objects based on the DataFrame's columns and their data types
columns = [Column(name, infer_sqlalchemy_type(dtype)) for name, dtype in df.dtypes.items()]

# Define a new table 'reviews' with the inferred columns
table = Table('reviews', metadata, *columns)

# Create the table in the database
table.create(engine)

# Insert the data from the DataFrame into the 'reviews' table
df.to_sql('reviews', con=engine, if_exists='append', index=False)

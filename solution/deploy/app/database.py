import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    """
    Establish a database connection and return the connection object.
    """
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn

def get_categories():
    """
    Fetches all categories from the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT category FROM reviews")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return {row['category']: row['category'] for row in rows}

def get_products(category):
    """
    Fetches all products for a given category from the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT product_name FROM reviews WHERE product_name is not null and category = %s", (category,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return {row['product_name']: row['product_name'] for row in rows}

def save_review(category, product, title, text, rating, sentiment):
    """
    Saves a review to the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reviews (category, product_name, reviews_title, reviews_text, rating, sentiment, reviews_date) VALUES (%s, %s, %s, %s, %s, %s, NOW())",
        (category, product, title, text, rating, sentiment)
    )
    conn.commit()
    cursor.close()
    conn.close()

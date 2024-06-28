import streamlit as st
import requests
from database import get_categories, get_products, save_review
from dotenv import load_dotenv
import os
import numpy as np
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

# Get API URL from environment variables
API_URL = os.getenv("API_URL", "http://localhost:8501/v1/models/sentiment_model:predict")

# Load the tokenizer
tokenizer_path = Path(__file__).parent / 'tokenizer.json'
with open(tokenizer_path) as f:
    data = f.read()
    tokenizer = tokenizer_from_json(data)

st.title("Review Sentiment Analysis")

# Initialize session state
if 'selected_category' not in st.session_state:
    st.session_state['selected_category'] = None
if 'selected_product' not in st.session_state:
    st.session_state['selected_product'] = None
if 'form_submitted' not in st.session_state:
    st.session_state['form_submitted'] = False
if 'sentiment' not in st.session_state:
    st.session_state['sentiment'] = None

# Category selection
categories = get_categories()
selected_category = st.selectbox("Select Category", options=list(categories.keys()), format_func=lambda x: categories[x])

# Update session state for selected_category
if selected_category != st.session_state['selected_category']:
    st.session_state['selected_category'] = selected_category
    st.session_state['selected_product'] = None  # Reset product when category changes

# Product selection based on selected category
if st.session_state['selected_category']:
    products = get_products(st.session_state['selected_category'])
else:
    products = {}

# Form for review submission
if not st.session_state['form_submitted']:
    with st.form(key='review_form'):
        if st.session_state['selected_category']:
            selected_product = st.selectbox("Select Product", options=list(products.keys()), format_func=lambda x: products[x])
        else:
            selected_product = None

        # Input fields for review title and text
        title = st.text_input("Review Title")
        review_text = st.text_area("Review Text")

        # Rating radio buttons
        rating = st.radio("Rating", options=[1, 2, 3, 4, 5], format_func=lambda x: f'{x} Star{"s" if x > 1 else ""}')

        # Submit button
        submit_button = st.form_submit_button(label='Submit Review')

        if submit_button:
            if title and review_text and selected_product and st.session_state['selected_category']:
                try:
                    # Tokenize and pad the review text
                    sequences = tokenizer.texts_to_sequences([review_text])
                    padded_sequences = pad_sequences(sequences, maxlen=200, padding='post', truncating='post')

                    # Call the model API to get sentiment
                    data = {
                        "instances": padded_sequences.tolist()
                    }
                    response = requests.post(API_URL, json=data)
                    response.raise_for_status()  # Raise an error for bad status codes
                    # Debug: Log the full response
                    st.write("Response status code:", response.status_code)
                    st.write("Response content:", response.json())

                    # Extract the sentiment prediction
                    predictions = response.json().get("predictions", [[0.0, 0.0, 0.0]])
                    sentiment_code = np.argmax(predictions[0])

                    # Interpret the sentiment code
                    if sentiment_code == 2:
                        sentiment = "positive"
                    elif sentiment_code == 0:
                        sentiment = "negative"
                    else:
                        sentiment = "neutral"

                    st.session_state['sentiment'] = sentiment

                    # Save the review data to the database
                    save_review(st.session_state['selected_category'], selected_product, title, review_text, rating, sentiment)

                    # Update session state to indicate form submission
                    st.session_state['form_submitted'] = True

                    # Display success message with sentiment
                    st.success(f"Thank you for your review! Sentiment: {sentiment}")

                    # Clear the form
                    st.rerun()
                except (requests.exceptions.RequestException, ValueError) as e:
                    st.error(f"Error fetching sentiment: {e}")
            else:
                st.error("Please fill in all fields.")
else:
    st.write("### Thank you for your review! Your feedback has been submitted.")
    st.write(f"Sentiment: {st.session_state['sentiment']}")
    # Button to reset the form
    if st.button("Submit Another Review"):
        st.session_state['form_submitted'] = False
        st.session_state['sentiment'] = None
        st.rerun()

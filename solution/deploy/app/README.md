# Sentiment LSTM 

This a simple application taht uses a LSTM model to predict the sentiment of a review. The model was trained using the Amazon Reviews Dataset. Docker image is based in TensorFlow Serving.

## Pre-requisites

- Docker
- Postgres Database - You can use seed.sql to create the tables and load the data

## How to run

1. Clone the repository
2. Run the following command to build the Docker image
```bash
docker build -t sentiment-lstm .
```
3. Run the following command to start the Docker container
```bash
docker run -e 'DATABASE_URL=postgresql://user:pass@host:port/database' -p 8502:8502 sentiment-lstm
```
4. Open your browser and go to http://localhost:8502

## How to use

1. Select a category
2. Select a product
3. Put a title
4. Put a review in the text area
5. Choose a rating
6. Click on the "Submit Review" button
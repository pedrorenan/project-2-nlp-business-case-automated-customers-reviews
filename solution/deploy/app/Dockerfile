# Base image for TensorFlow Serving
FROM tensorflow/serving:latest

# Install necessary packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    supervisor \
    && apt-get clean

# Install Streamlit and other dependencies
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

# Copy the saved model to the serving directory
COPY sentiment_model /models/sentiment_model/1
COPY sentiment_model/variables/variables.data-00000-of-00001 /models/sentiment_model/1/variables/variables.data-00000-of-00001

# Copy Streamlit app files
COPY app.py /app/app.py
COPY database.py /app/database.py
COPY tokenizer.json /app/tokenizer.json

# Copy Supervisor configuration
COPY supervisord.conf /etc/supervisor/supervisord.conf

# Copy the startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Set environment variables
ENV MODEL_NAME=sentiment_model

# Expose TensorFlow Serving port and Streamlit port
EXPOSE 8501
EXPOSE 8502

# Command to run Supervisor
ENTRYPOINT ["/start.sh"]
![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Project II | NLP Business Case: Automated Customers Reviews

## Executive Summary

This business case outlines the development of an NLP model to automate the processing of customer feedback for a retail company. The goal is to classify customer reviews into positive, negative, or neutral categories to help the company improve its products and services. The second part is to GenerativeAI to summarize reviews broken down into review score (0-5), and broken down into product categories - if the categories are too many to handle, select a top-K categories. Create a clickable and dynamic visualization dashboard using a tool like Tableau, Plotly, or any of your choice.

## Problem Statement

The company receives thousands of text reviews every month, making it challenging to manually categorize and analyze, and visualize them. An automated system can save time, reduce costs, and provide real-time insights into customer sentiment.


## Project goals

- The ML/AI system should be able to run classification of customers' reviews (the textual content of the reviews) into positive, neutral, or negative.
- For a product category, create a summary of all reviews broken down by each star or rating (we should have 5 of these).
  - If your system can't handle all products categories, pick a number that you can work with (eg top 10, top 50, Etc)

## Data Collection

- You may use the publicly available and downsized dataset of Amazon customer reviews from their online marketplace, such as the dataset found [here](https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products/data).
- You also pick any product reviews datasets from [here](https://huggingface.co/datasets/amazon_us_reviews). Make sure your computing resources can handle both your dataset size and the machine learning processes you will follow. 

## Traditional NLP & ML approaches - **20 points**

### 1. Data Preprocessing

#### 1.1 Data Cleaning

- Removed special characters, punctuation, and unnecessary whitespace from the text data.
- Converted text to lowercase to ensure consistency in word representations.

#### 1.2 Tokenization and Lemmatization

- Tokenized the text data to break it into individual words or tokens.
- Applied lemmatization to reduce words to their base or root form for better feature representation.

#### 1.3 Vectorization

- Used techniques such as CountVectorizer or TF-IDF Vectorizer to convert text data into numerical vectors.
- Created a document-term matrix representing the frequency of words in the corpus.

### 2. Model Building

### 2.1 Model Selection

- Explored different machine learning algorithms for text classification, including:
  - Naive Bayes
  - Logistic Regression
  - Support Vector Machines
  - Random Forest
- Evaluated each algorithm's performance using cross-validation and grid search for hyperparameter tuning.

### 2.2 Model Training
- Selected the best-performing algorithm based on evaluation metrics such as accuracy, precision, recall, and F1-score.
- Trained the selected model on the preprocessed text data.

### 3. Model Evaluation

#### 3.1 Evaluation Metrics

- Evaluated the model's performance on a separate test dataset using various evaluation metrics:
  - Accuracy: Percentage of correctly classified instances.
  - Precision: Proportion of true positive predictions among all positive predictions.
  - Recall: Proportion of true positive predictions among all actual positive instances.
  - F1-score: Harmonic mean of precision and recall.
- Calculated confusion matrix to analyze model's performance across different classes.

#### 3.2 Results

- Model achieved an accuracy of X% on the test dataset.
 - Precision, recall, and F1-score for each class are as follows:
 - Class 1: Precision=X%, Recall=X%, F1-score=X%
 - Class 2: Precision=X%, Recall=X%, F1-score=X%
 - ...
- Confusion matrix showing table and graphical representations

<br>

### Sequence-to-Sequence modeling with LSTM - **10 points**

Build a Biderectional LSTM model to predict the review class i.e., negative, positive, or neutral.

### Transformer approach (HuggingFace API) - **50 points**

A classification model, a summarirazation, and a dashboard are expected in this section.

### 1. Data Preprocessing

#### 1.1 Data Cleaning and Tokenization

- Cleaned and tokenized the customer review data to remove special characters, punctuation, and unnecessary whitespace.
- Applied tokenization using the tokenizer provided by the HuggingFace Transformers API to convert text data into input tokens suitable for model input.

#### 1.2 Data Encoding and Padding

- Encoded the tokenized input sequences into numerical IDs using the tokenizer's vocabulary.
- Padded input sequences to a maximum length to ensure uniform input size across samples.

### 2. Model Building

#### 2.1 Model Selection 

- Explored transformer-based models available in the HuggingFace Transformers API, including:
  - BERT (Bidirectional Encoder Representations from Transformers)
  - RoBERTa (Robustly Optimized BERT Approach)
  - DistilBERT (Lightweight version of BERT)
  - ...
- Selected a pre-trained transformer model suitable for text classification tasks, and justify your choice.
- Share the accuracy using the pre-trained model on your data **without** fine-tuning. This is your base model

#### 2.2 Model Fine-Tuning

- Fine-tuned the selected pre-trained model on the customer review dataset using transfer learning.
- Configured the fine-tuning process by specifying parameters such as batch size, learning rate, and number of training epochs.

### 3. Model Evaluation

#### 3.1 Evaluation Metrics

- Evaluated the base model and the fine-tuned model's performance on a separate validation dataset using standard evaluation metrics:
  - Accuracy: Percentage of correctly classified instances.
  - Precision: Proportion of true positive predictions among all positive predictions.
  - Recall: Proportion of true positive predictions among all actual positive instances.
  - F1-score: Harmonic mean of precision and recall.
- Calculated confusion matrix to analyze model's performance across different classes.

#### 3.2 Results 

- Model achieved an accuracy of X% on the validation dataset.
- Precision, recall, and F1-score for each class are as follows:
  - Class 1: Precision=X%, Recall=X%, F1-score=X%
  - Class 2: Precision=X%, Recall=X%, F1-score=X%
  - ...
- Confusion matrix

#### Deliverables - **20 points** 

- A PDF report documenting the approach, results, and analysis (**10 points**)
- Reproducible source code (jupyter notebook or .py files)
- PPT presentation - **No more than 20 minutes presentation** (**10 points**)
- Deploy your model in web app using the framework of your choice. 
- Bonus: host your app somewhere so it can be queried by anyone? (**5 points**)


<span style="color:red; weight: bold;">Passing Score is 70 points</span>.

You're expected to work in group of no more than 3 people. But given our number, I'd expect to see ONE group with 4 students. **You must work in a group**.

Your presentation should be tailored toward a technical and a non-technical audience. Feel free to reference "Create Presentation" guidelines provided in the Student Portal.
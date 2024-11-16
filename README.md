# Fraud Detection API Project

This repository contains a comprehensive project for fraud detection, including exploratory data analysis (EDA), model training and evaluation, and a deployed API for real-time fraud detection.

## **Project Structure**

```bash
.
├── fraud_detection_api/
│   ├── app.py              # Main application file
│   ├── serve_model.py      # API implementation for model predictions
│   ├── Dockerfile          # Configuration for containerizing the application
│
├── notebooks/
│   ├── Task_1.ipynb        # Exploratory Data Analysis (EDA)
│   ├── Task_2_and_3.ipynb  # Model comparison and interoperability
│
└── README.md               # Project documentation
```

## Overview

This project is designed to analyze and detect fraudulent activities using machine learning. It is divided into two main parts:

  1. API for Fraud Detection:
        - Provides an endpoint for real-time predictions based on input features.
        - Built using FastAPI and containerized using Docker for seamless deployment.

  2. Data Analysis and Model Development:
        - Detailed exploratory data analysis (EDA) to understand patterns and insights.
        - Comparison of multiple models to choose the best-performing one for predictions.
        - Implementation of model interoperability for seamless integration into the API.

## **Directories**
1. fraud_detection_api

   This directory contains the implementation of the fraud detection API:

      - app.py: The entry point for the FastAPI application.
      - serve_model.py: Contains the core logic for serving the model and handling predictions.
      - Dockerfile: A configuration file to containerize the API using Docker.

2. notebooks

   This directory includes Jupyter notebooks for EDA and model development:

   - Task_1.ipynb:
     
        - Performs exploratory data analysis to identify trends and relationships in the dataset.
        - Highlights key features and distributions affecting fraud detection.

   - Task_2_and_3.ipynb:
     
        - Compares the performance of multiple machine learning models.
        - Implements model interoperability for deployment.


## Getting Started
 Prerequisites

    Python 3.10+
    Docker (optional, for containerization)
    FastAPI
    Jupyter Notebook

Installation

    Clone the repository:

```bash
      git clone https://github.com/your_username/fraud_detection_api.git
      cd fraud_detection_api
```
Create and activate a virtual environment:
```bash
      python -m venv .venv
      source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
Install dependencies:

     pip install -r requirements.txt

## Running the API

   Start the API locally:
  
       uvicorn app:app --reload

   Alternatively, use Gunicorn:

       gunicorn -w 4 -b 0.0.0.0:8000 serve_model:app

       Access the API at http://127.0.0.1:8000.
 
   Using Docker

       Build the Docker image:

       docker build -t fraud_detection_api .

   Run the container:

       docker run -p 8000:8000 fraud_detection_api

## API Endpoints

    GET /:
        Health check endpoint to confirm the API is running.
        Returns: "Fraud Detection API is running"

    POST /predict:
        Accepts numeric input features for fraud detection.
        Returns: Predicted fraud score as a numeric value.

## Notebooks

  Task_1.ipynb:
  
        Conducts detailed exploratory data analysis.
        Visualizations and statistical summaries of the data.

  Task_2_and_3.ipynb:
  
        Compares models (e.g., Random Forest, Logistic Regression, etc.).
        Evaluates metrics like accuracy, precision, recall, and ROC-AUC.
        Integrates the best model for deployment in the API.

## Contributions

Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements.
License

This project is licensed under the MIT License. See the LICENSE file for details.


This can be directly copied and pasted into your GitHub repository's README file. It ensures clear headings and proper formatting for code and directory structures.



# serve_model.py
from flask import Flask, request, jsonify
import joblib
import numpy as np
import logging

app = Flask(__name__)

# Load the model
model = joblib.load("path/to/your_model.pkl")

# Setup logging
logging.basicConfig(level=logging.INFO)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        logging.info(f"Prediction made: {prediction[0]} for input {data['features']}")
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'API is healthy'}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify
from flask_cors import CORS
from joblib import load
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains and routes

# Load the trained model
model = load('random_forest_canola_model.joblib')

# Placeholder function to encode categorical features
# Replace or extend this with actual encoding logic
def encode_features(variety, product_name_rate, product_name_rate_2,product_name_rate_3, fert_name_rate):
    # Example encoding logic; replace with your actual encoding
    encoded_variety = 0  # Use your actual encoding mechanism here
    encoded_product_name_rate = 0  # Use your actual encoding mechanism here
    encoded_product_name_rate_2 = 0# Use your actual encoding mechanism here
    encoded_product_name_rate_3 = 0  # Use your actual encoding mechanism here
    encoded_fert_name_rate = 0  # Use your actual encoding mechanism here
    return [encoded_variety, encoded_product_name_rate, encoded_product_name_rate_2, encoded_product_name_rate_3, encoded_fert_name_rate]

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            
            # Extract features from incoming JSON and create a DataFrame
            # Ensure the order and names of features match those used during model training
            features_df = pd.DataFrame([{
                'acres_planted': data.get('acres_planted'),
                'days_to_harvest': data.get('days_to_harvest'),
                'variety': data.get('variety'),  # Assume these are already appropriately encoded
                'product_name_rate': data.get('product_name_rate'),
                'product_name_rate_2': data.get('product_name_rate_2'),
                'product_name_rate_3': data.get('product_name_rate_3'),
                'fert_name_rate': data.get('fert_name_rate'),
                # Add other features as needed
            }])
            
            # If necessary, encode categorical features here as you did during model training
            
            # Make a prediction using the DataFrame
            prediction = model.predict(features_df)
            return jsonify({'prediction': prediction.tolist()})
        except Exception as e:
            return jsonify({'error': f'Error making prediction: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
from joblib import load
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains and routes

# Load the trained model
model = load('random_forest_canola_model.joblib')


def encode_features(variety, product_name_rate, product_name_rate_2,product_name_rate_3, fert_name_rate):
    # encoding logic; 
    encoded_variety = 0  
    encoded_product_name_rate = 0  
    encoded_product_name_rate_2 = 0
    encoded_product_name_rate_3 = 0  
    encoded_fert_name_rate = 0  
    return [encoded_variety, encoded_product_name_rate, encoded_product_name_rate_2, encoded_product_name_rate_3, encoded_fert_name_rate]

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            
            # Extract features from incoming JSON and create a DataFrame
            features_df = pd.DataFrame([{
                'acres_planted': data.get('acres_planted'),
                'days_to_harvest': data.get('days_to_harvest'),
                'variety': data.get('variety'),  
                'product_name_rate': data.get('product_name_rate'),
                'product_name_rate_2': data.get('product_name_rate_2'),
                'product_name_rate_3': data.get('product_name_rate_3'),
                'fert_name_rate': data.get('fert_name_rate'),
              
            }])
            
            
            # Make a prediction using the DataFrame
            prediction = model.predict(features_df)
            return jsonify({'prediction': prediction.tolist()})
        except Exception as e:
            return jsonify({'error': f'Error making prediction: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)

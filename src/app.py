from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os

app = Flask(__name__, template_folder='src/templates')  # Adjust folder if needed

# Load the complete pipeline (preprocessing + model) from the pickle file
# Make sure the path is correct relative to the app root
model = joblib.load('model/wine_quality_pipeline.pkl')

@app.route("/")
def index():
    # Render the HTML UI
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # This endpoint only accepts POST requests for prediction
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    # Extract and convert the input features (all 11 features)
    try:
        fixed_acidity = float(data['fixed_acidity'])
        volatile_acidity = float(data['volatile_acidity'])
        citric_acid = float(data['citric_acid'])
        residual_sugar = float(data['residual_sugar'])
        chlorides = float(data['chlorides'])
        free_sulfur_dioxide = float(data['free_sulfur_dioxide'])
        total_sulfur_dioxide = float(data['total_sulfur_dioxide'])
        density = float(data['density'])
        pH = float(data['pH'])
        sulphates = float(data['sulphates'])
        alcohol = float(data['alcohol'])
    except KeyError as e:
        return jsonify({"error": f"Missing feature: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": f"Invalid value: {str(e)}"}), 400

    # Create the input array (ensure the order matches the pipeline's expectation)
    input_data = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                             chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
                             density, pH, sulphates, alcohol]])

    # Get the prediction from the pipeline
    prediction = model.predict(input_data)
    predicted_quality = int(prediction[0])  # Convert numpy.int64 to a Python int

    # Create a descriptive message (assumes model returns 1 for good and 0 for bad quality)
    result = "Good Quality Wine" if predicted_quality == 1 else "Bad Quality Wine"
    return jsonify({"predicted_quality": result})

if __name__ == '__main__':
    # Bind to the port provided by the environment (for deployment) or default to 5000 for local testing.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

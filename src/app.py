from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os

# Set the template folder path relative to this file's location
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
app = Flask(__name__, template_folder=template_dir)

# Load the complete pipeline (preprocessing + model) from the pickle file
model = joblib.load('model/wine_quality_pipeline.pkl')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Ensure the request is JSON
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    # Extract and convert the input features (all 11 features)
    try:
        fixed_acidity = float(data["fixed_acidity"])
        volatile_acidity = float(data["volatile_acidity"])
        citric_acid = float(data["citric_acid"])
        residual_sugar = float(data["residual_sugar"])
        chlorides = float(data["chlorides"])
        free_sulfur_dioxide = float(data["free_sulfur_dioxide"])
        total_sulfur_dioxide = float(data["total_sulfur_dioxide"])
        density = float(data["density"])
        pH = float(data["pH"])
        sulphates = float(data["sulphates"])
        alcohol = float(data["alcohol"])
    except KeyError as e:
        return jsonify({"error": f"Missing feature: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": f"Invalid value: {str(e)}"}), 400

    # Create the input array (the order must match what your pipeline expects)
    input_data = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                             chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
                             density, pH, sulphates, alcohol]])

    # Get the prediction from the pipeline
    prediction = model.predict(input_data)
    predicted_quality = int(prediction[0])  # Convert numpy.int64 to a Python int

    # Create a descriptive message based on the prediction
    result = "Good Quality Wine" if predicted_quality == 1 else "Bad Quality Wine"
    return jsonify({"predicted_quality": result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)

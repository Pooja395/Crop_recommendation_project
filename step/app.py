from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Initialize Flask App
app = Flask(__name__, template_folder="templates", static_folder="static")

# Load Trained Model
model = joblib.load("crop_recommendation_model.pkl")
print("Model loaded successfully!")

# Route to Serve HTML Page
@app.route("/")
def home():
    return render_template("index.html")  # Serve the index.html file

# API Route for Prediction
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Parse Input JSON
        data = request.json
        features = np.array([[data['N'], data['P'], data['K'], data['temperature'],
                              data['humidity'], data['pH'], data['rainfall']]])
        prediction = model.predict(features)
        return jsonify({"Recommended Crop": prediction[0]})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

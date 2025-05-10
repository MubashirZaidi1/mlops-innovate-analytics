from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model_path = os.path.join("mlflow", "models", "random_forest.pkl")
model = joblib.load(model_path)

@app.route("/")
def home():
    return "✅ ML model server is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

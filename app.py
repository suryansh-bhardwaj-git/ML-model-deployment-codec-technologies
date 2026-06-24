from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

MODEL_FILE = "iris_model.pkl"

# Train model if not already saved
if not os.path.exists(MODEL_FILE):
    iris = load_iris()

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(iris.data, iris.target)
    joblib.dump(model, MODEL_FILE)

# Load model
model = joblib.load(MODEL_FILE)

app = Flask(__name__)

species = [
    "Setosa",
    "Versicolor",
    "Virginica"
]

@app.route("/")
def home():
    return {
        "project": "Cloud-Based ML Model Deployment",
        "status": "Running"
    }

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    features = [[
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"]
    ]]

    prediction = model.predict(features)[0]

    return jsonify({
        "prediction": species[prediction]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
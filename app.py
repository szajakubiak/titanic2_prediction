from flask import Flask, request, jsonify
import json
import calculate
import numpy as np

app = Flask(__name__)

@app.route("/example", methods = ["GET"])
def example():
    return jsonify({"Age": 38,
                    "Pclass": 2,
                    "SibSp": 0,
                    "Parch": 1,
                    "Fare": 30.00,
                    "Sex": "male",
                    "Embarked": "S"})


@app.route("/predict", methods = ["POST"])
def predict():
    input_data = request.get_json()

    result = calculate.prediction(input_data)

    return jsonify({"Survival rate": np.float64(result)})


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
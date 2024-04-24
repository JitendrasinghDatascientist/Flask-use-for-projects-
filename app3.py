import pandas as pd
from flask import Flask, request, jsonify,render_template
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

data = [
    {'glucose_level': 85, 'blood_pressure': 80, 'insulin': 0, 'bmi': 22, 'diabetes': 0},
    {'glucose_level': 168, 'blood_pressure': 74, 'insulin': 0, 'bmi': 35, 'diabetes': 1},
]

df = pd.DataFrame(data)
X = df.drop("diabetes", axis=1)
Y = df["diabetes"]
model = LinearRegression()
model.fit(X, Y)

@app.route("/Diabetes_prediction", methods=["POST"])
def diabetes_prediction():
    content = request.json
    health_metrics = content["health_metrics"]
    prediction = prediction_diabetes_risk(health_metrics)
    return jsonify({"prediction": prediction})

def prediction_diabetes_risk(health_metrics):
    df = pd.DataFrame(health_metrics)
    prediction = model.predict(df)
    if prediction == 1:
        return "You may have diabetes."
    else:
        return "You may not have diabetes."
@app.route("/")
def index():
    return render_template("Diabetes.html")

if __name__ == "__main__":
    app.run(debug=True)

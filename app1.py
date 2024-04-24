from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Train the model
data = [
    {'prolonged_fever': 1, 'headache': 1, 'fatigue': 1, 'abdominal_pain': 1, 'diarrhea': 1, 'rash': 0, 'typhoid': 1},
    {'prolonged_fever': 1, 'headache': 1, 'fatigue': 1, 'abdominal_pain': 1, 'diarrhea': 0, 'rash': 1, 'typhoid': 1},
    {'prolonged_fever': 0, 'headache': 0, 'fatigue': 0, 'abdominal_pain': 0, 'diarrhea': 0, 'rash': 0, 'typhoid': 0},
    {'prolonged_fever': 0, 'headache': 0, 'fatigue': 0, 'abdominal_pain': 0, 'diarrhea': 1, 'rash': 0, 'typhoid': 0}
]
df = pd.DataFrame(data)
X = df.drop("typhoid", axis=1)
Y = df["typhoid"]
model = LinearRegression()
model.fit(X, Y)

# Endpoint to predict typhoid
@app.route('/predict_typhoid', methods=['POST'])
def predict_typhoid():
    content = request.json
    health_metrics = content['health_metrics']
    prediction = prediction_risk_typhoid(health_metrics)
    return jsonify({'prediction': prediction})

# Function to predict typhoid
def prediction_risk_typhoid(health_metrics):
    df = pd.DataFrame([health_metrics])
    prediction = model.predict(df)
    if prediction == 1:
        return "You have a risk of Typhoid. Please consult your doctor."
    else:
        return "You are fine."

# Route to render Typhoid.html template
@app.route('/')
def index():
    return render_template('Typhoid.html')

if __name__ == '__main__':
    app.run(debug=True)


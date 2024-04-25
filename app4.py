import pandas as pd
from flask import Flask , request, jsonify, render_template
from sklearn.linear_model import LinearRegression 
app = Flask(__name__)
data = [
    {"Age_Gap":10,"Education":20,"Independent":90,"Marriage":0},
    {"Age_Gap":10,"Education":20,"Independent":90,"Marriage":1}
]
df = pd.DataFrame(data)
X = df.drop("Marriage",axis=1)
Y = df["Marriage"]
model = LinearRegression()
model.fit(X,Y)
@app.route("/Marriage_prediction",methods=["POST"])
def Marriage_prediction():
    content = request.json
    Marriage_data = content["Marriage_data"]
    prediction = prediction_on_marriage(Marriage_data)
    return jsonify({"prediction":prediction})

def prediction_on_marriage(Marriage_data):
    df = pd.DataFrame(Marriage_data)
    prediction = model.predict(df)
    if prediction > 0.5:
        return "you are  single"
    else:
        return "you are not single"

@app.route("/")
def index():
    return render_template("Marriage.html")
if __name__ =="__main__":
    app.run(debug=True)
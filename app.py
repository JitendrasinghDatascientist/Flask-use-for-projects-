from flask import Flask, render_template, request

app = Flask(__name__)

def predict_salary(experience, project_completed):
    return 5000 * experience + 5000 * project_completed + 5

@app.route("/", methods=["GET", "POST"])
def salary():
    prediction = None
    if request.method == "POST":
        experience = float(request.form["experience"])
        project_completed = int(request.form["project_completed"]) 
        prediction = predict_salary(experience, project_completed)
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)


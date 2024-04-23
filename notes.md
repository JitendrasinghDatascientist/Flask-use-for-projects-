from flask import Flask, redirect, url_for,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/success/<int:score>")
def success(score):
    return "The person should be passed " + str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The person should be failed " + str(score)

@app.route("/results/<int:marks>")
def results(marks):
    if marks > 33:
        return redirect(url_for('success', score=marks))
    else:
        return redirect(url_for('fail', score=marks))
@app.route("/",methods=["GET","POST"])
def addition():
    if request.method=="POST":
        num1 = request.form.get("num1",type=int)
        num2 = request.form.get("num2",type=int)
        result = num1 + num2
    return render_template("index.html",result=result)



if __name__=="__main__":
    app.run(debug=True)
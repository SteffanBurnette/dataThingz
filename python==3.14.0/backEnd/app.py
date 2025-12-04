from flask import Flask, render_template, request, redirect, url_for

#Create the instance of the flask class will act as
# your WSGI (Web server Gateway Interface) application
app = Flask(__name__)

# Note that routes are deorators in flask
@app.route("/")
def welcome():
    return "<html><H1>Welcome soilder</H1></html>"

@app.route("/index", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form", methods = ["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello {name}"
    return render_template("form.html")

@app.route("/submit2", methods = ["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello {name}"
    return render_template("form.html")

# Variable Rule
@app.route("/successtest/<score>")
def success(score):
    return "You got a score of " + score + " on you final exam."

@app.route("/successtest2/<int:score>")
def success2(score):
    return f"You got a score of {score} on your final exam. NIOCE"


@app.route("/success/<int:score>")
def success3(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"

    exp = {"score": score, "res": res}

    return render_template("result1.html", results = exp)

# If conditional in html file
@app.route("/successif/<int:score>")
def successif(score):

    return render_template("result2.html", results = score)

@app.route("/fail/<int:score>")
def fail(score):

    return render_template("result3.html", results = score)

@app.route("/submit", methods = ["POST", "GET"])
def get_results():
    total_score = 0

    if request.method == "POST":
        science = float(request.form["science"])
        maths = float(request.form["maths"])
        c = float(request.form["c"])
        data_science = float(request.form["datascience"])

        total_score = (science + maths + c + data_science)/4
    else:
        return render_template("getresult.html")
    return redirect(url_for("successif", score = total_score))


if __name__ == "__main__":
    app.run(debug = True)
# debug = True makes the server automatically restart everytime a change is made
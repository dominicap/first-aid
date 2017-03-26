from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hello.html")

@app.route("/results", methods = ["GET", "POST"])
def results():
    if request.method == "POST":
        return "Submit accomplished!"
    else:
        return "whut.."

from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html.j2")

@app.route("/results", methods = ["GET", "POST"])
def results():
    if request.method == "POST":
        return render_template("results.html.j2", request=request)
    else:
        return "whut.."

app.run(debug=True)

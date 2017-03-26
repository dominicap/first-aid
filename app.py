from flask import Flask, url_for, request, render_template
from lib import request_data as req_data
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html.j2")

@app.route("/results", methods = ["GET", "POST"])
def results():
    query = request.form["input"]
    key_words = req_data.key_words_from_query(query)
    
    if request.method == "POST":
        return render_template("results.html.j2", request=request)
    else:
        return "whut.."

app.run(debug=True)

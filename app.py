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
    key_words_tokens = req_data.string_to_tokens(query)

    results_dict = req_data.results_to_dict(req_data.search_grid(key_words))

    relevant_result = req_data.get_relevant_result(results_dict, key_words_tokens)

    if request.method == "POST":
        return render_template("results.html.j2", query=query, relevant_result=relevant_result)
    else:
        return "Request not received."

app.run(debug=True)

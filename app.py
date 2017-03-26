import json
import random
import urllib

from flask import Flask, url_for, request, render_template
from lib import request_data as req_data

app = Flask(__name__)

@app.route("/")
def index():
    sayings = ['What is on your mind?', 'What is your question?', 'Have any doubts?', "What is your problem today?", "What is frustrating you today?s"]
    return render_template("index.html.j2", saying=random.choice(sayings))

@app.route("/results", methods = ["GET", "POST"])
def results():
    query = request.form["input"]
    key_words = req_data.key_words_from_query(query)
    key_words_tokens = req_data.string_to_tokens(query)

    results_dict = req_data.results_to_dict(req_data.search_grid(key_words))

    try:
        relevant_result = req_data.get_relevant_result(results_dict, key_words_tokens)

        if __get_key(relevant_result, 'description') is not None:
            description = __get_key(relevant_result, 'description')
        else:
            description = ""

        if __get_key(relevant_result, 'title') is not None:
            title = __get_key(relevant_result, 'title')
        else:
            title = query

    except ValueError:
        return "Request does not exist."

    if request.method == "POST":
        return render_template("results.html.j2", title=title, relevant_result=relevant_result, description=description)
    else:
        return "Request not received."

def __get_key(youtube_url, key):
    video_id = youtube_url.replace("https://www.youtube.com/embed/", '').strip()
    url = 'https://www.khanacademy.org/api/v1/user/videos/' + video_id

    result = None

    try:
        result = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))['video'][key]
    except urllib.error.HTTPError as exception:
        if exception.code == 404:
            print("JSON not available for " + url)
    except KeyError:
        print("Key does not exist for video " + url)

    return result

app.run(debug=True)

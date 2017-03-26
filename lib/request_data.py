import json
import spacy
import requests

from nltk.stem.porter import *
from string import punctuation

nlp = spacy.load('en')

stemmer = PorterStemmer()
translator = str.maketrans('', '', punctuation)

def key_words_from_query(query):
    tokens = nlp.tokenizer(query.translate(translator).strip().lower())
    return [stemmer.stem(str(token)) for token in tokens if not token.is_stop]

big_parser_file = open("../.keys/BIGPARSER_KEYS", "r")

BIGPARSER_CREDENTIALS = list(big_parser_file.read().splitlines())
GRID_ID = "58d77d20478af70572b61145"
URL = "https://www.bigparser.com/APIServices/api/"

data = {
  "emailId": BIGPARSER_CREDENTIALS[0],
  "password": BIGPARSER_CREDENTIALS[1],
  "loggedIn": True
}

login_data_json = json.dumps(data)
login_headers = {'Content-type': 'application/json'}
authID = requests.post(URL + 'common/login', data=login_data_json, headers=login_headers).json()['authId']

def search_grid(key_words):

    search_data = {
      "gridId": GRID_ID,
      "viewId": None,
      "selectColumnsStoreName": [],
      "rowCount": 10,
      "sortKeys": [],
      "tags": [],
      "keywords": key_words
    }

    search_data_json = json.dumps(search_data)
    search_headers = {'authId': authID, 'Content-type': 'application/json'}
    search_results = requests.post(URL + 'query/table', data=search_data_json, headers=search_headers).json()

    print(search_results["rows"])

    print(results_to_dict(search_results))

def results_to_dict(results):
    result_dictionary = {}

    for result in results["rows"]:
        for data in result:
            result_dictionary[result["data"][0]] = result["data"][1]

    return result_dictionary


search_grid(key_words_from_query('integral'))

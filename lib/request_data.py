import json
import spacy
import requests

from nltk.stem.porter import *
from string import punctuation

nlp = spacy.load('en')

stemmer = PorterStemmer()
translator = str.maketrans('', '', punctuation)

def key_words_from_query(query):
    tokens = string_to_tokens(query)
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

    return search_results

def results_to_dict(results):
    result_dictionary = {}

    for result in results["rows"]:
        for data in result:
            result_dictionary[result["data"][0]] = result["data"][1]

    return result_dictionary

def get_relevant_result(result_dictionary, query):
    keys = result_dictionary.keys()
    values = result_dictionary.values()

    cleansed_values = []
    for value in values:
        cleansed_values.append(value.split('|'))

    tokenized_values = []
    for value in cleansed_values:
        token_string = ' '.join(value)
        tokenized_values.append(string_to_tokens(token_string))

    scores = []
    for value in tokenized_values:
        scores.append(value.similarity(query))

    keys = list(keys)
    return keys[scores.index(max(scores))]

def string_to_tokens(string):
    tokens = nlp.tokenizer(string.translate(translator).strip().lower())
    return tokens


print(get_relevant_result(results_to_dict(search_grid(key_words_from_query("what is a differential equation"))), string_to_tokens("what is alpha and beta particle")))

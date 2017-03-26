import spacy

from nltk.stem.porter import *
from string import punctuation

nlp = spacy.load('en')

stemmer = PorterStemmer()
translator = str.maketrans('', '', punctuation)

def key_words_from_query(query):
    tokens = nlp.tokenizer(query.translate(translator).strip().lower())
    return [stemmer.stem(str(token)) for token in tokens if not token.is_stop]

def search_grid(key_words):
    # Get results

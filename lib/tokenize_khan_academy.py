import spacy

from string import punctuation
from nltk.stem.porter import *

stemmer = PorterStemmer()
translator = str.maketrans('', '', punctuation)

nlp = spacy.load('en')
tokens = nlp.tokenizer(description.translate(translator).strip().lower())

keywords = [stemmer.stem(str(token)) for token in tokens if not token.is_stop]

print(keywords)

import json
import spacy
import urllib.request

from string import punctuation
from nltk.stem.porter import *

nlp = spacy.load('en')

stemmer = PorterStemmer()
translator = str.maketrans('', '', punctuation)

with open('../data/video_links.txt', 'r') as file:
    links = file.readlines()

descriptions = []
for link in links:
    video_id = link.replace('http://youtube.com/watch?v=', '').strip()
    url = 'https://www.khanacademy.org/api/v1/user/videos/' + video_id
    try:
        results = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
        descriptions.append(results['video']['description'])
    except urllib.error.HTTPError as exception:
        if exception.code == 404:
            print("JSON not avaiable for " + url)
    except KeyError:
        print("Key does not exist for video " + url)

for description in descriptions:
    tokens = nlp.tokenizer(description.translate(translator).strip().lower())

    with open('../data/link_keywords.txt', 'w+') as file:
        file.write([stemmer.stem(str(token)) for token in tokens if not token.is_stop])

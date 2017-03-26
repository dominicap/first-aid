import json
import spacy
import urllib.request

from nltk.stem.porter import *
from string import punctuation

nlp = spacy.load('en')

stemmer = PorterStemmer()
translator = str.maketrans('', '', punctuation)

with open('../data/txt/video_links.txt', 'r') as file:
    links = [line.rstrip() for line in file.readlines()]

empty_urls = []
descriptions = []
for link in links:
    video_id = link.replace('http://youtube.com/watch?v=', '').strip()
    url = 'https://www.khanacademy.org/api/v1/user/videos/' + video_id

    try:
        results = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
        descriptions.append(results['video']['description'])
    except urllib.error.HTTPError as exception:
        if exception.code == 404:
            print("JSON not available for " + url)
            empty_urls.append(url.replace('https://www.khanacademy.org/api/v1/user/videos/', 'http://youtube.com/watch?v='))
    except KeyError:
        print("Key does not exist for video " + url)

relevant_links = []
for link in links:
    if link not in empty_urls:
        relevant_links.append(link)

with open('../data/txt/relevant_video_links.txt', 'a+') as file:
    for relevant_link in relevant_links:
        file.write(relevant_link + '\n')

for description in descriptions:
    tokens = nlp.tokenizer(description.translate(translator).strip().lower())

    with open('../data/txt/link_keywords.txt', 'a+') as file:
        delimited_string = ""
        for keyword in [stemmer.stem(str(token)) for token in tokens if not token.is_stop]:
            delimited_string = delimited_string + "|" + keyword
        delimited_string = delimited_string[1:]
        file.write(delimited_string + '\n')

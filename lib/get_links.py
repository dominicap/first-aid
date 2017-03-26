import json
import math
import urllib.request

youtube_key_file = open("../.keys/YOUTUBE_KEYS", "r")

YOUTUBE_CREDENTIALS = str(youtube_key_file.read().strip())
KHAN_ACADEMY_CHANNEL_ID = 'UC4a-Gbdw7vOaccHmFo40b9g'

PAGE_TOKEN = ''
TOTAL_RESULTS = 50

result_level = 1
while (result_level <= math.ceil(float(TOTAL_RESULTS) / 50.0)):

    URL = "https://www.googleapis.com/youtube/v3/search?key=" + YOUTUBE_CREDENTIALS + "&channelId=" + KHAN_ACADEMY_CHANNEL_ID + "&part=snippet,id&order=date&maxResults=50&pageToken=" + PAGE_TOKEN
    results = json.loads(urllib.request.urlopen(URL).read().decode('utf-8'))

    try:
        PAGE_TOKEN = results['nextPageToken']
    except KeyError:
        print('REQUEST LIMIT')
        quit()

    if (result_level == 1):
        TOTAL_RESULTS = int(results['pageInfo']['totalResults'])

    for result in results['items']:
        with open('../data/txt/video_links.txt', 'a+') as file:
            try:
                file.write("http://youtube.com/watch?v=" + result['id']['videoId'] + '\n')
            except KeyError:
                print("Key does not exist for result " + result)

    result_level = result_level + 1

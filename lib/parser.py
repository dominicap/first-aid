import json
import math
import urllib.request

youtube_key_file = open("../.keys/YOUTUBE_KEYS", "r")

YOUTUBE_CREDENTIALS = str(youtube_key_file.read().strip())
KHAN_ACADEMY_CHANNEL_ID = 'UC4a-Gbdw7vOaccHmFo40b9g'
PAGE_TOKEN = ''

TOTAL_RESULTS = 10

result_level = 1
while (result_level <= math.ceil(float(TOTAL_RESULTS) / 50.0)):
    print("At level " + str(result_level))

    URL = "https://www.googleapis.com/youtube/v3/search?key=" + YOUTUBE_CREDENTIALS + "&channelId=" + KHAN_ACADEMY_CHANNEL_ID + "&part=snippet,id&order=date&maxResults=50&pageToken" + PAGE_TOKEN

    results = json.loads(urllib.request.urlopen(URL).read().decode('utf-8'))

    if (result_level == 1):
        PAGE_TOKEN = results['nextPageToken']
        TOTAL_RESULTS = int(results['pageInfo']['totalResults'])

    for result in results['items']:
        with open('../data/video_ids.txt', 'a+') as file:
            file.write(result['id']['videoId'] + '\n')

    result_level = result_level + 1

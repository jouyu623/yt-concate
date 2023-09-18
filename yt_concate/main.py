import urllib.request
import json
from yt_concate.settings import API_KEY #yt_concate.settings 是絕對路徑
print(API_KEY)# 官方提供的管道給你拿取東西，要自己申請複製憑證，不要推到GitHub上讓大家一直來用

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'  # 上網查詢的網址的channel id

def get_all_video_in_channel(channel_id):

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'  # 讓我們使用API的網址

    first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                        channel_id)
    # 使用API時要拿的網址，排序方式Channel ID = KEy+Value

    video_links = []
    url = first_url  # 餵資料給url
    while True:  # 拿資料直到沒有為止
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']  # 找不到nextPageToken就跳出迴圈
            url = first_url + '&pageToken={}'.format(next_page_token)
        except KeyError:  # 所有錯誤都中斷跳出執行
            break
    return video_links


video_list = get_all_video_in_channel(CHANNEL_ID)
print(len(video_list))

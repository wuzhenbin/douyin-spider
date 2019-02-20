


import time
import re
import aiohttp, asyncio
from pymongo import MongoClient
import requests
import json
from requests.exceptions import RequestException


headers = {
    'Host':	'v3-dy.ixigua.com',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G955N Build/NRD90M)',
    'X-SS-TC': '0',
    'X-Gorgon':	'03dd560d44004290e020ad792277b4859bd7c857242a0b120416',
    'X-Khronos': '1550646834',
    'Connection': 'keep-alive'
}

def get_response(url):
    try:
        response = requests.get(url,headers=headers)
        print(response)
        if response.status_code == 200:
            return response.content
        return None
    except RequestException as e:
        print('err: %s' % e)

client = MongoClient('localhost', 27017)
db = client['douyin']
mongo_table = 'user_video'

lis = db[mongo_table].find_one({ 'uid': '101209612312' })
video_lis = [ item['url'] for item in lis['video_list'] ]


test = video_lis[0]
print(test)
# html = get_response(test)
# print(html)



# async def fn(url,sem):
#     async with sem:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url) as resp:
#                 filename = resp.headers['media-length'] + str(int(time.time()))
#                 # 获取视频后缀
#                 video_info = resp.headers['Content-Type']
#                 pattern = re.compile('video/(.*)', re.S)
#                 results = re.findall(pattern,video_info)
#                 nail = results[0]
#                 with open('{}.{}'.format(filename,nail), 'wb') as fd:
#                     while True:
#                         chunk = await resp.content.read()
#                         if not chunk:
#                             break
#                         fd.write(chunk)


# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     sem = asyncio.Semaphore(3)
#     tasks = [ asyncio.ensure_future(fn(item,sem)) for item in lis]
#     loop.run_until_complete(asyncio.wait(tasks))

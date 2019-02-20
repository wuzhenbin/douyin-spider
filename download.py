


import time
import re
import aiohttp, asyncio
from pymongo import MongoClient
import requests
import json
from requests.exceptions import RequestException


mac_proxies = {
    'http':  '127.0.0.1:1087',
    'https': '127.0.0.1:1087'
}


headers = {
    'method': 'GET',
    'authority': 'aweme.snssdk.com',
    'scheme': 'https',
    'path': '/aweme/v1/play/?video_id=v0200f0e0000bhkl3kmgnco4vjqi6big&line=0&ratio=540p&watermark=1&media_type=4&vr_type=0&test_cdn=None&improve_bitrate=0&logo_name=aweme_suffix&device_platform=android&device_type=MIX+2S&version_code=511&device_id=59892667972&channel=xiaomi&aid=1128&pass-region=1&pass-route=1',
    'cookie':  'uid_tt=30926ae0391cf3e9e834dd45a24aab69',
    'cookie':  'sid_tt=d41022f0bafa6da72719701709fa1671',
    'cookie':  'sessionid=d41022f0bafa6da72719701709fa1671',
    'cookie':  'sid_guard=d41022f0bafa6da72719701709fa1671%7C1546133120%7C5184000%7CThu%2C+28-Feb-2019+01%3A25%3A20+GMT',
    'cookie':  'odin_tt=140719de27757e23bf31974dd3b07cd911e3a7b1b9c3682fa7e558c3c07c04fb1072a674459ae12d1a457285724acb62961666157d9c1de6aaf7f5646cfa0ca0',
    'cookie':  'install_id=63988049034',
    'cookie':  'ttreq=1$6cbbf87ea620092943f5c73405c068da3115e710',
    'cookie':  'qh[360]=1',
    'accept-encoding': 'gzip',
    'x-ss-req-ticket': '1550669825897',
    'x-tt-token':  '00d41022f0bafa6da72719701709fa167155b85afd8e380ca407f3f6e2dee2e67f231adf62847faa0f4bf3c450629e4b9125',
    'sdk-version': '1',
    'user-agent':  'com.ss.android.ugc.aweme/511 (Linux; U; Android 9; zh_CN; MIX 2S; Build/PKQ1.180729.001; Cronet/58.0.2991.0)',
    'x-khronos':  '1550669825',
    'x-gorgon': '030086d600008df6a47c513cfc4e4eefb804de9cf08454c9c704',
    'x-pods': ''
}

def get_response(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        print('err: %s' % e)

client = MongoClient('localhost', 27017)
db = client['douyin']
mongo_table = 'user_video'

lis = db[mongo_table].find_one({ 'uid': '101209612312' })
video_lis = [ item['url'] for item in lis['video_list'] ]


# test_url = 'https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200f0e0000bhkl3kmgnco4vjqi6big&line=0&ratio=540p&watermark=1&media_type=4&vr_type=0&test_cdn=None&improve_bitrate=0&logo_name=aweme_suffix&device_platform=android&device_type=XT1570&version_code=510&device_id=66402745074&channel=wandoujia_aweme&aid=1128&pass-region=1&pass-route=1'

test_url = 'https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200f0e0000bhkl3kmgnco4vjqi6big&line=0&ratio=540p&watermark=1&media_type=4&vr_type=0&test_cdn=None&improve_bitrate=0&logo_name=aweme_suffix&device_platform=android&device_type=MIX+2S&version_code=511&device_id=59892667972&channel=xiaomi&aid=1128&pass-region=1&pass-route=1'
# print(test_url)
html = get_response(test_url)
print(html)

# https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200f0e0000bhkl3kmgnco4vjqi6big&line=0&ratio=540p&watermark=1&media_type=4&vr_type=0&test_cdn=None&improve_bitrate=0&logo_name=aweme

# https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200f0e0000bhkl3kmgnco4vjqi6big&line=0&ratio=540p&watermark=1&media_type=4&vr_type=0&test_cdn=None&improve_bitrate=0&logo_name=aweme_suffix&device_platform=android&device_type=XT1570&version_code=510&device_id=66402745074&channel=wandoujia_aweme&aid=1128&pass-region=1&pass-route=1


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

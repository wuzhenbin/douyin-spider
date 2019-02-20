
# mitmdump -s mitmdump-script.py
import json
from mitmproxy import ctx
from utils import *

def response(flow):
    user_1 = 'https://api-eagle.amemv.com/aweme/v1/user'
    user_2 = 'https://aweme-eagle.snssdk.com/aweme/v1/user'       
    if flow.request.url.startswith(user_1) or flow.request.url.startswith(user_2):
        text = flow.response.text
        data = json.loads(text)

        unique_id = data['user']['unique_id']
        uid = data['user']['uid']
        nickname = data['user']['nickname']
        signature = data['user']['signature']
        birthday = data['user']['birthday'] 
        country = data['user']['country'] 
        avatar = data['user']['avatar_larger']['url_list']
        result = {
            'unique_id': unique_id,
            'uid': uid,
            'nickname': nickname,
            'signature': signature,
            'birthday': birthday,
            'country': country,
            'avatar': avatar,
        }
        mongo_example = mongoCls()
        mongo_example.save_to_mongo(result,{'key': 'uid', 'val': uid})
        
    
    video_list_1 = 'https://api.amemv.com/aweme/v1/aweme/post'   
    video_list_2 = 'https://aweme.snssdk.com/aweme/v1/aweme/post'              
    if flow.request.url.startswith(video_list_1) or flow.request.url.startswith(video_list_2):
        text = flow.response.text
        data = json.loads(text)
        lis = data['aweme_list'] if len(data['aweme_list']) > 0 else []
        if len(lis)>0:
            lis = list(filter(lambda item: 'video' in item, lis))

            video_list = [{ 'url': item['video']['play_addr']['url_list'][0], 'aweme_id': item['aweme_id'] } for item in lis]
            uid = data['aweme_list'][0]['author']['uid']
            result = {
                'video_list': video_list,
                'uid': uid
            }

            mongo_example = mongoCls()
            mongo_example.save_to_mongo(result,{'key': 'uid', 'val': uid})


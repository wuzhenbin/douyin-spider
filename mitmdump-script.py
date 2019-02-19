

# mitmdump -s mitmdump-script.py
import json
from mitmproxy import ctx
from pymongo import MongoClient

MONGO_URL = 'localhost:27017'
MONGO_DB = 'douyin'
MONGO_TABLE = 'user_video'


class mongoCls:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]

    def read_one(self, condition={}):
        return self.db[MONGO_TABLE].find_one(condition)

    def save_to_mongo(self, result, id_dict):
        key = id_dict['key']
        val = id_dict['val']
        res = self.read_one({key: val})
        if res:
            for item,val in result.items():
                res[item] = val

            if self.db[MONGO_TABLE].update({key: val}, {'$set': res}):
                print('update cuccessful', result)
                return True

        else:
            if self.db[MONGO_TABLE].insert(result):
                print('save cuccessful', result)
                return True
            return False

def response(flow):
    user_detail_url = 'https://aweme-eagle.snssdk.com/aweme/v1/user/'       
    if flow.request.url.startswith(user_detail_url):
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
        

    user_video_url = 'https://api.amemv.com/aweme/v1/aweme/post'  
    if flow.request.url.startswith(user_video_url):
        text = flow.response.text
        data = json.loads(text)
        lis = data['aweme_list'] if len(data['aweme_list']) > 0 else []
        if len(lis)>0:
            lis = list(filter(lambda item: 'video' in item, lis))

            video_list = [item['video']['play_addr']['url_list'][0] for item in lis]
            uid = data['aweme_list'][0]['author']['uid']
            result = {
                'video_list': video_list,
                'uid': uid
            }

            mongo_example = mongoCls()
            mongo_example.save_to_mongo(result,{'key': 'uid', 'val': uid})






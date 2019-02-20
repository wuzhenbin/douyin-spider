
import sys
sys.path.append('c:\\users\\yx2018011502\\anaconda3\\lib\\site-packages')
from pymongo import MongoClient
from collections import OrderedDict

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
            # 筛选更新字段
            for item,val in result.items():
                # 如果是视频字段有内容 
                if item=='video_list' and 'video_list' in res:
                    merge_list = res['video_list'] + val
                    res_lis_dict = OrderedDict()
                    for item in merge_list:
                        res_lis_dict.setdefault(item['aweme_id'], {**item})

                    res['video_list'] = list(res_lis_dict.values())

                else:
                    res[item] = val

            if self.db[MONGO_TABLE].update({key: val}, {'$set': res}):
                print('update cuccessful', result)
                return True

        else:
            if self.db[MONGO_TABLE].insert(result):
                print('save cuccessful', result)
                return True
            return False

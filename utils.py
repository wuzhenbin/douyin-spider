
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
import platform

if 'Windows' in platform.system():
    sys.path.append('c:\\users\\yx2018011502\\anaconda3\\lib\\site-packages')
    
from pymongo import MongoClient
from collections import OrderedDict

MONGO_URL = 'localhost:27017'
MONGO_DB = 'douyin'
MONGO_TABLE = 'user_video'


DRIVER_SERVER = 'http://localhost:4723/wd/hub'
TIMEOUT = 300
# 上拉间隔
SCROLL_SLEEP_TIME = 0.5


PLATFORM = "Android"
DEVICENAME = "127.0.0.1:62001"

NORESET = "true"


class appAction:
    def __init__(self, APPPACKAGE, APPACTIVITY):
        # 驱动配置
        self.desired_caps = {
            'platformName': PLATFORM,
            'deviceName': DEVICENAME,
            'appPackage': APPPACKAGE,
            'appActivity': APPACTIVITY,
            'noReset': NORESET
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)


    # 获取屏幕尺寸
    def GetPageSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    '''
        上滑 （俗称上拉加载更多）
            技巧：上滑是从较大y值--->较小y值 
            技巧：上滑时x轴值基本无变化 

            技巧：sx的值可s[0]范围内随意
            因为需要考虑：状态条、导航栏、底部功能栏等所占数值
    '''
    def swipe_up(self):
        s = self.GetPageSize()
        sx = s[0] * 0.43
        sy = s[1] * 0.9
        ex = s[0] * 0.43
        ey = s[1] * 0.2
        self.driver.swipe(sx, sy, ex, ey, duration=time.sleep(0.2))

    '''
        下滑（俗称下拉刷新）
        技巧：sx的值可s[0]范围内随意，sy和ey 需在 s[1]*0.2 -- s[1]-s[1]*0.4 之间取值，
        因为需要考虑：状态条、导航栏、底部功能栏等所占数值
    '''
    def swipe_down(self):
        s = self.GetPageSize()
        sx = s[0] * 0.35
        sy = s[1] * 0.35
        ex = s[0] * 0.35
        ey = s[1] * 0.75
        self.driver.swipe(sx, sy, ex, ey, duration=time.sleep(1))

    '''
        技巧：左滑是从较大x值 --->较小x值
        技巧：左滑时y轴值基本无变化，所以ey=0
        技巧：sx的值一定大于屏幕尺寸的53%，否则虽向左滑动但不能生效切换页面
        例子为边缘左滑
    '''
    def swipe_left(self):
        s = self.GetPageSize()
        sx = s[0] * 0.99
        sy = s[1] * 0.75
        ex = s[0] * 0.8
        ey = s[1] * 0.75
        self.driver.swipe(sx, sy, ex, ey, duration=time.sleep(1))

    '''
        技巧：sx的值一定不能大于屏幕尺寸的 46%，否则虽然向右滑动但不能生效切换页面
    '''
    def swipe_right(self):
        s = self.GetPageSize()
        sx = s[0] * 0.01
        sy = s[1] * 0.75
        ex = s[0] * 0.8
        ey = s[1] * 0.25
        self.driver.swipe(sx, sy, ex, ey, duration=time.sleep(1))


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

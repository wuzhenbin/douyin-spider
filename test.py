import requests
import json
from requests.exceptions import RequestException
from pyquery import PyQuery as pq

def get_response(url):
    try:
        response = requests.get(url,headers=list_headers)
        if response.status_code == 200:
            return response.json()
        return None
    except RequestException as e:
        print('err: %s' % e)


def video_list():
    html = get_response('https://aweme.snssdk.com/aweme/v1/aweme/post/?max_cursor=0&user_id=101209612312&count=20&retry_type=no_retry&mcc_mnc=46007&iid=63723769089&device_id=62694298322&ac=wifi&channel=wandoujia_aweme&aid=1128&app_name=aweme&version_code=500&version_name=5.0.0&device_platform=android&ssmix=a&device_type=SM-G955N&device_brand=samsung&language=zh&os_api=19&os_version=4.4.2&uuid=354730010762049&openudid=4ccc6ad65e7f1920&manifest_version_code=500&resolution=720*1280&dpi=240&update_version_code=5002&_rticket=1550555361125&ts=1550555359&as=a1850906efbd4c482b2888&cp=96d3c756f0b86b81e1ckko&mas=0143e90b1d1b4e780af8f90260ce42be2d1c1c1c4c464c1c2cc62c')

    print(html)

def user_detail():
    html = get_response('https://aweme-eagle.snssdk.com/aweme/v1/user/?user_id=101209612312&retry_type=no_retry&mcc_mnc=46007&iid=63723769089&device_id=62694298322&ac=wifi&channel=wandoujia_aweme&aid=1128&app_name=aweme&version_code=500&version_name=5.0.0&device_platform=android&ssmix=a&device_type=SM-G955N&device_brand=samsung&language=zh&os_api=19&os_version=4.4.2&uuid=354730010762049&openudid=4ccc6ad65e7f1920&manifest_version_code=500&resolution=720*1280&dpi=240&update_version_code=5002&_rticket=1550555360517&ts=1550555359&as=a1a509e65f3dec588b2888&cp=94d2cb5bf7b46e86e1ckko&mas=01254f2555254fe77bf9b979aa30244fd91c1c1c4c461c1cacc6a6')

    html = get_response()
    

    print(html)
    # nickname = html['user']['nickname']
    # signature = html['user']['signature']
    # birthday = html['user']['birthday'] 
    # country = html['user']['country'] 
    # cover_url = html['cover_url']

    # print(nickname)
    # print(signature)
    # print(birthday)
    # print(country)
    # print(avatar)

def user_search():
    html = get_response('https://aweme.snssdk.com/aweme/v1/general/search/single/?keyword=h_kyung_176&offset=0&count=10&is_pull_refresh=0&hot_search=0&latitude=33.999704&longitude=114.569088&ts=1550558115&js_sdk_version=&app_type=normal&openudid=4ccc6ad65e7f1920&version_name=5.0.0&device_type=SM-G955N&ssmix=a&iid=63723769089&os_api=19&mcc_mnc=46007&device_id=62694298322&resolution=720*1280&device_brand=samsung&aid=1128&manifest_version_code=500&app_name=aweme&_rticket=1550558118461&os_version=4.4.2&device_platform=android&version_code=500&update_version_code=5002&ac=wifi&dpi=240&uuid=354730010762049&language=zh&channel=wandoujia_aweme&as=a1150a06437a3c539b2699&cp=aeaac2523eb46130e1qkyo&mas=01b91d0dbf91c947f21816f9cd66c6a1af9c9c6c4c469cccacc6cc')
    
    print(html)

if __name__ == '__main__':
    user_search()
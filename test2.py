


from cls import download
import json
import requests
from utils import *

mongoCls_ins = mongoCls()
res = mongoCls_ins.read_one({'uid': '62166516505'})
lis = res['video_list'][:10]

def main():
    for item in lis:
	    url = item['url']
	    download_cls = download(url=url)
	    download_cls.down_video()


if __name__ == '__main__':
    main()
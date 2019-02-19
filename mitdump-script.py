

# mitmdump -s mitmdump-script.py
import json
from mitmproxy import ctx

def response(flow):
    url = 'https://aweme.snssdk.com/aweme/v1/general/search/single/'
    if flow.request.url.startswith(url):
        text = flow.response.text
        print(text)
        # data = json.loads(text)
        # if data.get('floors') and len(data.get('floors'))>0:
        #     index = len(data.get('floors')) - 1
        #     info = data.get('floors')[index].get('data')
        #     name = info.get('wareInfo')['name']
        #     images = info.get('wareImage')
        #     data_info = {
        #         'name': name,
        #         'images': images
        #     }
        #     print(data_info)

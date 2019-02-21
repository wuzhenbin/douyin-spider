
import os
import requests
from requests.exceptions import RequestException
from hashlib import md5
import json

class download:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    }

    def save_file(self,content):
        file_create = '/' + self.file_name 
        file_path = '{0}/{1}.{2}'.format(os.getcwd() + file_create,md5(content).hexdigest(),self.format)
        if not os.path.exists(file_path):
            with open(file_path,'wb') as f:
                f.write(content)
                f.close()

    def get_response(self):
        try:
            response = requests.get(self.url,headers=self.headers)
            if response.status_code == 200:
                self.save_file(response.content)
            return None
        except RequestException:
            print("请求失败~")
            return None

    def __init__(self, content="",url="", format="",save_file_name="./result.txt",filePath="./result.txt"):
        self.content = content
        self.url = url
        self.format = format
        self.save_file_name = save_file_name 
        self.filePath = filePath

    def read_to_file(self):
        with open(self.filePath, encoding='UTF-8') as f:
            data = f.read()
            return json.loads(data) 

    def write_to_file(self):
        with open(self.save_file,'a',encoding='utf-8') as f:
            f.write(json.dumps(self.content, ensure_ascii=False) + '\n')
            f.close()

    def down_video(self):
        self.format = 'mp4'
        self.file_name = 'video'
        os.system('mkdir {}'.format(self.file_name))
        self.get_response()

    def down_image(self):
        self.format = 'jpg'
        self.file_name = 'image'
        os.system('mkdir {}'.format(self.file_name))
        self.get_response()

    


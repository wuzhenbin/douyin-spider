
import time
import re
import aiohttp, asyncio
from utils import *
from tqdm import tqdm

# mongoCls_ins = mongoCls()
# res = mongoCls_ins.read_one({'uid': '62166516505'})
# lis = res['video_list'][:10]

lis = [
    {
        'aweme_id': '11',
        'url': 'http://192.168.124.81:8080/11.mp4',
    },
    {
        'aweme_id': '12',
        'url': 'http://192.168.124.81:8080/12.mp4',
    },
    {
        'aweme_id': '13',
        'url': 'http://192.168.124.81:8080/13.mp4',
    },
    {
        'aweme_id': '14',
        'url': 'http://192.168.124.81:8080/14.mp4',
    },
    {
        'aweme_id': '15',
        'url': 'http://192.168.124.81:8080/15.mp4',
    },
    {
        'aweme_id': '16',
        'url': 'http://192.168.124.81:8080/16.mp4',
    },
    {
        'aweme_id': '17',
        'url': 'http://192.168.124.81:8080/17.mp4',
    },
    {
        'aweme_id': '18',
        'url': 'http://192.168.124.81:8080/18.mp4',
    },
    {
        'aweme_id': '19',
        'url': 'http://192.168.124.81:8080/19.mp4',
    },
    {
        'aweme_id': '20',
        'url': 'http://192.168.124.81:8080/20.mp4',
    },
    {
        'aweme_id': '20',
        'url': 'http://192.168.124.81:8080/20.mp4',
    },
    {
        'aweme_id': '21',
        'url': 'http://192.168.124.81:8080/21.mp4',
    },
    {
        'aweme_id': '22',
        'url': 'http://192.168.124.81:8080/22.mp4',
    },
    {
        'aweme_id': '23',
        'url': 'http://192.168.124.81:8080/23.mp4',
    }
]

async def fn(item,sem):
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.get(item['url']) as resp:
                filename = item['aweme_id']
                # 获取视频后缀
                if 'Content-Type' in resp.headers:
                    video_info = resp.headers['Content-Type']
                    pattern = re.compile('video/(.*);', re.S)
                    results = re.findall(pattern,video_info)
                    nail = results[0]
                    time.sleep(1)
                    with open('{}.{}'.format(filename,nail), 'wb') as fd:
                        while True:
                            chunk = await resp.content.read()
                            if not chunk:
                                break
                            fd.write(chunk)

                print('None')

def main():
    loop = asyncio.get_event_loop()
    sem = asyncio.Semaphore(2)
    tasks = [asyncio.ensure_future(fn(item,sem)) for item in lis]
    
    with tqdm(total=len(lis)) as pbar:
        for task in tasks:
            task.add_done_callback(lambda _: pbar.update(1))

        loop.run_until_complete(asyncio.wait(tasks))

        

if __name__ == '__main__':
    main()


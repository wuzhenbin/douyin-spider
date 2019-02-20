
import time
import aiohttp, asyncio
from pymongo import MongoClient
from tqdm import tqdm


client = MongoClient('localhost', 27017)
db = client['douyin']
mongo_table = 'user_video'

async def dowload_task(item,sem):
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.get(item['url']) as resp:
                filename = item['aweme_id']
                with open('{}.mp4'.format(filename), 'wb') as fd:
                    while True:
                        chunk = await resp.content.read()
                        if not chunk:
                            break
                        fd.write(chunk)

def download():
    res = db[mongo_table].find_one({ 'uid': '101209612312' })
    lis = res['video_list']
    loop = asyncio.get_event_loop()
    sem = asyncio.Semaphore(3)
    tasks = [ asyncio.ensure_future(dowload_task(item,sem)) for item in tqdm(lis)]
    loop.run_until_complete(asyncio.wait(tasks))

if __name__ == '__main__':
    download()


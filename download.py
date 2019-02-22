
import time
import re
import aiohttp, asyncio
from utils import *
from tqdm import tqdm

mongoCls_ins = mongoCls()
res = mongoCls_ins.read_one({'uid': '50751958524'})
lis = res['video_list']


async def fn(item,sem):
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.get(item['url'][0]) as resp:
                filename = item['aweme_id']
                # 获取视频后缀
                video_info = resp.headers['Content-Type']
                pattern = re.compile('video/(.*)', re.S)
                results = re.findall(pattern,video_info)
                nail = results[0]
                with open('{}.{}'.format(filename,nail), 'wb') as fd:
                    while True:
                        chunk = await resp.content.read()
                        if not chunk:
                            break
                        fd.write(chunk)

def main():
    loop = asyncio.get_event_loop()
    sem = asyncio.Semaphore(3)
    tasks = [asyncio.ensure_future(fn(item,sem)) for item in lis]
    
    with tqdm(total=len(lis)) as pbar:
        for task in tasks:
            task.add_done_callback(lambda _: pbar.update(1))

        loop.run_until_complete(asyncio.wait(tasks))

if __name__ == '__main__':
    main()


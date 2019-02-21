
from utils import *
from tqdm import tqdm
import aiohttp, asyncio

mongoCls_ins = mongoCls()
res = mongoCls_ins.read_one({'uid': '62166516505'})
item = res['video_list'][3]

# 单视频下载
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(item['url']) as resp:
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

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


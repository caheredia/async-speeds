import aiohttp
import asyncio
import time
import datetime
import uvloop
from clients.helpers import save_rate, get_row_count, find_rate

url = "http://127.0.0.1:5000/stamp"


async def curl(session, url, method="GET", json=None):
    async with session.request(method, url, json=json) as response:
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        runs = 100
        rows = 100
        for i in range(runs):
            tasks = []
            start = time.time()
            for i in range(rows):
                time_now = datetime.datetime.now().isoformat()
                payload = {"stamp": time_now}
                tasks.append(curl(session, url, "POST", json=payload))
            await asyncio.gather(*tasks)
            end = time.time()
            delta = end - start
            write_rate = find_rate(delta, rows)
            # save write speeds
            save_rate("aiohttp_uvloop_sanic", write_rate=write_rate)


if __name__ == "__main__":
    # print initial row count
    get_row_count("timestamps")

    uvloop.install()
    asyncio.run(main())

    get_row_count("timestamps")


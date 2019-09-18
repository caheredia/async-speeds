import aiohttp
import asyncio
import time
import datetime
import requests
import uvloop
from clients.helpers import save_rate, get_row_count

url = "http://127.0.0.1:5000/tag"
# url = "http://localhost:8000/tag"
save_url = "http://localhost:8000/save"


async def curl(session, url, method="GET", json=None):
    async with session.request(method, url, json=json) as response:
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        runs = 10
        rows = 10
        for i in range(runs):
            tasks = []
            start = time.time()
            for i in range(rows):
                time_now = datetime.datetime.now().isoformat()
                payload = {"tag": time_now}
                tasks.append(curl(session, url, "POST", json=payload))
            await asyncio.gather(*tasks)
            end = time.time()
            delta = end - start
            print(f"total time: {delta}")
            write_rate = int(rows / delta)
            print(f"Rows/second: {write_rate}")
            # save write speeds
            save_rate("aiohttp_flask", write_rate)


if __name__ == "__main__":
    # print initial row count
    get_row_count("hashtags")

    # uvloop.install()
    asyncio.run(main())

    get_row_count("hashtags")


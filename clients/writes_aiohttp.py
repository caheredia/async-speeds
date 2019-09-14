import aiohttp
import asyncio
import time
import datetime
import requests
import uvloop


time_now = datetime.datetime.now().isoformat()
url = "http://localhost:8000/tag"
save_url = "http://localhost:8000/save"


async def curl(session, url, method="GET", json=None):
    async with session.request(method, url, json=json) as response:
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        runs = 10
        rows = 100
        for i in range(runs):
            tasks = []
            start = time.time()
            for i in range(rows):
                payload = {"tag": time_now}
                tasks.append(curl(session, url, "POST", json=payload))
            await asyncio.gather(*tasks)
            end = time.time()
            delta = end - start
            print(f"total time: {delta}")
            write_rate = int(rows / delta)
            print(f"Rows/second: {write_rate}")
            # save write speeds
            write_payload = {"method": "aiohttp_sanic_uvloop", "rate": write_rate}
            await curl(session, save_url, method="POST", json=write_payload)


if __name__ == "__main__":
    r = requests.get("http://localhost:8000/total/hashtags")
    print("number of rows: ", r.json()["total"])
    uvloop.install()
    asyncio.run(main())
    r = requests.get("http://localhost:8000/total/hashtags")
    print("number of rows: ", r.json()["total"])


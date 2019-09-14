import requests_async as async_requests
import requests
import datetime
import asyncio
import time
import uvloop


time_now = datetime.datetime.now().isoformat()
url = "http://localhost:8000/tag"
save_url = "http://localhost:8000/save"


async def curl(url, json=None):
    await async_requests.post(url, json=json)


async def main():
    runs = 100
    rows = 100
    for i in range(runs):
        tasks = []
        start = time.time()
        for i in range(rows):
            payload = {"tag": time_now}
            tasks.append(curl(url, json=payload))
        await asyncio.gather(*tasks)
        end = time.time()
        delta = end - start
        print(f"total time: {delta}")
        write_rate = int(rows / delta)
        print(f"Rows/second: {write_rate}")
        # save write speeds
        write_payload = {"method": "async", "rate": write_rate}
        await curl(save_url, json=write_payload)


if __name__ == "__main__":
    r = requests.get("http://localhost:8000/total/hashtags")
    print("number of rows: ", r.json()["total"])
    # uvloop.install()
    asyncio.run(main())
    r = requests.get("http://localhost:8000/total/hashtags")
    print("number of rows: ", r.json()["total"])

import requests_async as async_requests
import datetime
import asyncio
import time
import uvloop
from sql.helpers import save_rate, get_row_count, find_rate


url = "http://127.0.0.1:5000/stamp"


async def curl(url, json=None):
    await async_requests.post(url, json=json)


async def main():
    runs = 10
    rows = 50
    for i in range(runs):
        tasks = []
        start = time.time()
        for i in range(rows):
            time_now = datetime.datetime.now().isoformat()
            payload = {"stamp": time_now}
            tasks.append(curl(url, json=payload))
        await asyncio.gather(*tasks)
        end = time.time()
        delta = end - start
        write_rate = find_rate(delta, rows)
        # save write speeds
        save_rate("async_flask", write_rate=write_rate)


if __name__ == "__main__":
    # print initial row count
    get_row_count("timestamps")

    uvloop.install()
    asyncio.run(main())

    # print final row count
    get_row_count("timestamps")

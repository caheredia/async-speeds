import aiohttp
import asyncio
import time
import datetime
import requests
import uvloop
import sqlite3


time_now = datetime.datetime.now().isoformat()
url = "http://localhost:8000/tag"


def save_rate(method, write_rate):
    """Save rates to rate table."""
    conn = sqlite3.connect("hashtag.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO rates VALUES (:method,:rate)",
        {"method": method, "rate": write_rate},
    )
    conn.commit()
    conn.close()


async def fetch(session, url):
    payload = {"tag": time_now}
    async with session.post(url, json=payload) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        runs = 100
        rows = 100
        for i in range(runs):
            tasks = []
            for i in range(rows):
                tasks.append(fetch(session, url))
            start = time.time()
            await asyncio.gather(*tasks)
            end = time.time()
            delta = end - start
            print(f"total time: {delta}")
            write_rate = int(rows / delta)
            print(f"Rows/second: {write_rate}")
            save_rate(method="aiohttp_uvloop", write_rate=write_rate)


if __name__ == "__main__":
    r = requests.get("http://localhost:8000/total")
    print("number of rows: ", r.text)
    uvloop.install()
    asyncio.run(main())

    r = requests.get("http://localhost:8000/total")
    print("number of rows: ", r.text)


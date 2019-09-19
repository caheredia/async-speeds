import requests
import datetime
import time
from clients.writes_sql import save_rate


url = "http://127.0.0.1:5000/"


r = requests.get(url + "total/timestamps")
print("number of rows: ", r.json()["total"])


def write(time_stamp):
    payload = {"tag": time_stamp}
    r = requests.post(url + "tag", json=payload)
    return r.json()


runs = 100
rows = 100
for i in range(runs):
    start = time.time()
    for i in range(rows):
        time_now = datetime.datetime.now().isoformat()
        write(time_now)
    end = time.time()
    delta = end - start
    print(f"total time: {delta}")
    write_rate = int(rows / delta)
    print(f"Rows/second: {write_rate}")
    # save write speeds
    save_rate("flask", write_rate=write_rate)


r = requests.get(url + "total/timestamps")
print("number of rows: ", r.json()["total"])

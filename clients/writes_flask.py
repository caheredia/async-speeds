import requests
import datetime
import time
from clients.helpers import save_rate, get_row_count, find_rate


url = "http://127.0.0.1:5000/"

# print initial row count
get_row_count("timestamps")


def write(time_stamp):
    payload = {"stamp": time_stamp}
    r = requests.post(url + "stamp", json=payload)
    return r.json()


runs = 10
rows = 100
for i in range(runs):
    start = time.time()
    for i in range(rows):
        time_now = datetime.datetime.now().isoformat()
        write(time_now)
    end = time.time()
    delta = end - start
    write_rate = find_rate(delta, rows)
    # save write speeds
    save_rate("requests_flask", write_rate=write_rate)


# print final row count
get_row_count("timestamps")

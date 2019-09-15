import requests
import datetime


time_now = datetime.datetime.now().isoformat()
url = "http://127.0.0.1:5000/"


r = requests.get(url + "total/hashtags")
print("number of rows: ", r.json()["total"])

payload = {"tag": time_now}
r = requests.post(url + "tag", json=payload)
print(r.json())

r = requests.get(url + "total/hashtags")
print("number of rows: ", r.json()["total"])

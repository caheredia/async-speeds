import requests
import datetime


time_now = datetime.datetime.now().isoformat()
url = "http://127.0.0.1:5000/"
save_url = "http://localhost:8000/save"

r = requests.get(url + "total")
print("number of rows: ", r.json()["total"])

from sanic import Sanic
from sanic.response import json
import aiosqlite

DATABASE = "sql/write-speeds.db"

app = Sanic(__name__)


@app.listener("before_server_start")
async def before_start(app, loop):
    print("SERVER STARTING")
    global db
    db = await aiosqlite.connect(DATABASE)


@app.listener("after_server_stop")
async def after_stop(app, loop):
    print("Closing connection to sqlite")
    await db.close()


@app.route("/stamp", methods=["POST"])
async def post(request):
    stamp = request.json["stamp"]
    await db.execute("INSERT INTO timestamps VALUES (:stamp)", {"stamp": stamp})
    await db.commit()
    return json({"saved": stamp}, status=201)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False, access_log=False)

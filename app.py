from sanic import Sanic
from sanic.response import json
import aiosqlite


app = Sanic(__name__)


@app.listener("before_server_start")
async def before_start(app, loop):
    print("SERVER STARTING")
    global db
    db = await aiosqlite.connect("hashtag.db")


@app.listener("after_server_stop")
async def after_stop(app, loop):
    print("Closing connection to sqlite")
    await db.close()


@app.route("/total/<table>", methods=["GET"])
async def post(request, table):
    cursor = await db.execute(f"SELECT COUNT(*) FROM {table}")
    rows = await cursor.fetchall()
    await cursor.close()
    return json({"total": rows[0][0]}, status=200)


@app.route("/tag", methods=["POST"])
async def post(request):
    tag = request.json["tag"]
    await db.execute(
        "INSERT INTO hashtags VALUES (:user,:category,:tag)",
        {"user": "xristian", "category": "leica", "tag": tag},
    )
    await db.commit()
    return json({"saved": tag}, status=201)


@app.route("/save", methods=["POST"])
async def save_rate(request):
    """Save rates to rate table."""
    method = request.json["method"]
    rate = request.json["rate"]
    await db.execute(
        "INSERT INTO rates VALUES (:method,:rate)", {"method": method, "rate": rate}
    )
    await db.commit()
    return json({"method": method, "rate": rate}, status=201)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False, access_log=False)

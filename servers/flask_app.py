from flask import Flask, jsonify, g, request
import sqlite3

DATABASE = "sql/write-speeds.db"
app = Flask(__name__)


def connect_db():
    return sqlite3.connect(DATABASE)


@app.before_request
def before_request():
    g.db = connect_db()


@app.route("/stamp", methods=["POST"])
def tag():
    stamp = request.json["stamp"]
    g.db.execute("INSERT INTO timestamps VALUES (:stamp)", {"stamp": stamp})
    g.db.commit()
    return jsonify({"saved": tag})


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, "db"):
        g.db.close()


if __name__ == "__main__":
    app.run(debug=False)

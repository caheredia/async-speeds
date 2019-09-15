from flask import Flask, jsonify, g
import sqlite3

DATABASE = "sql/hashtag.db"
app = Flask(__name__)


def connect_db():
    return sqlite3.connect(DATABASE)


@app.before_request
def before_request():
    g.db = connect_db()


@app.route("/total")
def total():
    c = g.db.execute("SELECT COUNT(*) FROM hashtags")
    results = c.fetchall()
    return jsonify({"total": results[0][0]})


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, "db"):
        g.db.close()


@app.route("/")
def hello_world():
    return jsonify({"message": "Hello, World!"})


if __name__ == "__main__":
    app.run(debug=True)

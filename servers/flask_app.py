from flask import Flask, jsonify, g, request
import sqlite3

DATABASE = "sql/write-speeds.db"
app = Flask(__name__)


def connect_db():
    return sqlite3.connect(DATABASE)


@app.before_request
def before_request():
    g.db = connect_db()


@app.route("/total/<table>")
def total(table):
    c = g.db.execute(f"SELECT COUNT(*) FROM {table}")
    results = c.fetchall()
    return jsonify({"total": results[0][0]})


@app.route("/tag", methods=["POST"])
def tag():
    tag = request.json["tag"]
    g.db.execute(
        "INSERT INTO hashtags VALUES (:user,:category,:tag)",
        {"user": "xristian", "category": "leica", "tag": tag},
    )
    g.db.commit()
    return jsonify({"saved": tag})


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, "db"):
        g.db.close()


if __name__ == "__main__":
    app.run(debug=False)

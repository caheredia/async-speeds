from servers.flask_app import app

total_url = "http://localhost:8000/total"

tables = ["/hashtags", "/rates"]


def test_root():
    for table in tables:
        _, response = app.test_client.get("http://127.0.0.1:5000/ ")
        assert response.json == "Hello, World!"


def test_api_ping(client):
    res = client.get(url_for("api.pi"))
    assert res.json == {"ping": "pong"}


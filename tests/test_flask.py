from servers.flask_app import app
import pytest


@pytest.fixture(scope="module")
def test_client():
    flask_app = app

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


def test_hello(test_client):
    res = test_client.get("/")
    assert res.json["message"] == "Hello, World!"


def test_total(test_client):
    res = test_client.get("/total")
    total = res.json['total']
    assert isinstance(total,int)


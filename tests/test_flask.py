from servers.flask_app import app
import pytest

tables = ["/hashtags", "/rates"]


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


def test_total(test_client):
    for table in tables:
        res = test_client.get(f"/total{table}")
        total = res.json["total"]
        assert isinstance(total, int)


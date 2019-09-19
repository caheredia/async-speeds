from sql.helpers import get_row_count
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


def test_stamp_response(test_client):
    payload = {"stamp": "test"}
    res = test_client.post("/stamp", json=payload)
    assert res.json["saved"] == "test"


def test_stamp_increase(test_client):
    """Test that after /stamp post absolute number of rows in db increased by 1."""
    # fetch pre total
    total_pre = get_row_count("timestamps")
    # add row to database
    payload = {"stamp": "test"}
    test_client.post("/stamp", json=payload)
    # fetch post total

    total_post = get_row_count("timestamps")

    assert total_post == total_pre + 1

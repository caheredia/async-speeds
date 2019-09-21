from servers.sanic_app import app
from sql.helpers import get_row_count

url = "/stamp"


def test_stamp_status():
    payload = {"stamp": "test"}
    _, response = app.test_client.post(url, json=payload)
    assert response.status == 201


def test_stamp_response():
    payload = {"stamp": "test"}
    _, response = app.test_client.post(url, json=payload)
    assert response.json["saved"] == "test"


def test_stamp_increase():
    """Test that after /stamp post absolute number of rows in db increased by 1."""
    # fetch pre total
    total_pre = get_row_count("timestamps")
    # add row to database
    payload = {"stamp": "test"}
    _, save_response = app.test_client.post(url, json=payload)
    # fetch post total

    total_post = get_row_count("timestamps")

    assert total_post == total_pre + 1

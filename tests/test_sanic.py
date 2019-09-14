from app import app

total_url = "http://localhost:8000/total"

tables = ['/hashtags', '/rates']

def test_total():
    _, response = app.test_client.get(total_url)
    assert response.status == 200


def test_total_type():
    for table in tables:
        _, response = app.test_client.get(total_url+table)
        r = response.json["total"]
        assert isinstance(r, int)


save_url = "http://localhost:8000/save"


def test_save_status():
    payload = {"write_method": "test", "rate": 0}
    _, response = app.test_client.post(save_url, json=payload)
    assert response.status == 201


def test_save():
    payload = {"write_method": "test", "rate": 0}
    _, response = app.test_client.post(save_url, json=payload)
    assert response.json[0] == "saved"


tag_url = "http://localhost:8000/tag"


def test_tag_status():
    payload = {"tag": "test"}
    _, response = app.test_client.post(tag_url, json=payload)
    assert response.status == 201


def test_tag_response():
    payload = {"tag": "test"}
    _, response = app.test_client.post(tag_url, json=payload)
    assert response.json["saved"] == "test"


def test_tag_increase():
    """Test that after save absolute number of rows in db increased by 1."""
    # fetch pre total
    _, pre_response = app.test_client.get(total_url+'/hashtags')
    total_pre = pre_response.json["total"]
    # add row to database
    payload = {"tag": "test"}
    _, save_response = app.test_client.post(tag_url, json=payload)
    # fetch post total
    _, post_response = app.test_client.get(total_url+'/hashtags')
    total_post = post_response.json["total"]
    assert total_post == total_pre + 1

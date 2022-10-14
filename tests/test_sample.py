import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from app import app
import json
test_client = app.test_client()

def test_index_response_OK():
    assert test_client.get("/").status == "200 OK"

def test_data_response_OK():
    assert test_client.get("/data").status == "200 OK"

def test_constituencies_response_OK():
    constituencies = []
    constituencies_path = os.path.join("tests", "constituencies.json")
    with open(constituencies_path) as f_in:
        constituencies = json.loads(f_in.read())["constituencies"]
    
    for constituency in constituencies:
        path = "/results/{}".format(constituency)
        assert test_client.get(path).status == "200 OK"


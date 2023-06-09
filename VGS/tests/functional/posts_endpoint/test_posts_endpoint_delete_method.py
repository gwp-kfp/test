import requests

from lib.constants import posts_endpoint


# Validate the status code of the response when making delete request to the "posts" endpoint is 200
def test_response_status_code_is_200():
    response = requests.delete("{}/0".format(posts_endpoint))
    assert response.status_code == 200


# Validate the content type of the response when making delete request to the "posts" endpoint is json
def test_response_content_type_is_json():
    response = requests.delete("{}/0".format(posts_endpoint))
    assert "application/json" in response.headers["Content-Type"]


# Validate the json schema of the response when making a delete request to the "posts" endpoint
def test_response_json_schema_validation():
    response = requests.delete("{}/0".format(posts_endpoint))
    assert response.json() == {}


# Validate number of items returned in the response when making a delete request to the "posts" endpoint
def test_number_of_items_returned():
    response = requests.delete("{}/0".format(posts_endpoint))
    assert len(response.json()) == 0

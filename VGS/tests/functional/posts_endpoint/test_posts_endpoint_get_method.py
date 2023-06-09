import requests

from lib.aux import validate_posts_endpoint_response_json_schema
from lib.constants import posts_endpoint


# Validate the status code of the response when making get request to the "posts" endpoint is 200
def test_response_status_code_is_200():
    response = requests.get(posts_endpoint)
    assert response.status_code == 200


# Validate the status code of the response when retrieving a valid post is 200
def test_valid_post_response_status_code_is_200():
    response = requests.get("{}/1".format(posts_endpoint))
    assert response.status_code == 200


# Validate the status code of the response when retrieving a valid post is 404
def test_invalid_post_response_status_code_is_404():
    response = requests.get("{}/1000".format(posts_endpoint))
    assert response.status_code == 404


# Validate the content type of the response when making get request to the "posts" endpoint is json
def test_response_content_type_is_json():
    response = requests.get(posts_endpoint)
    assert "application/json" in response.headers["Content-Type"]


# Validate the json schema of the response when making a get request to the "posts" endpoint
def test_response_json_schema_validation():
    response = requests.get(posts_endpoint)
    assert validate_posts_endpoint_response_json_schema(response.json())


# Validate the total number of posts returned in the response when making a get request to the "posts" endpoint
def test_number_of_posts_returned():
    response = requests.get(posts_endpoint)
    assert len(response.json()) == 100

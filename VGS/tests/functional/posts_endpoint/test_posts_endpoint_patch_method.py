import requests

from lib.aux import validate_posts_endpoint_response_json_schema
from lib.constants import posts_endpoint, posts_endpoint_patch_method_request_json


# Validate the status code of the response when making patch request to update a valid post is 200
def test_valid_post_response_status_code_is_200():
    response = requests.patch("{}/1".format(posts_endpoint))
    assert response.status_code == 200


# Validate the status code of the response when making patch request to update a non-existent post is 200
def test_invalid_post_response_status_code_is_200():
    response = requests.patch("{}/1000".format(posts_endpoint))
    assert response.status_code == 200


# Validate the content type of the response when making patch request to the "posts" endpoint is json
def test_response_content_type_is_json():
    response = requests.patch("{}/1".format(posts_endpoint))
    assert "application/json" in response.headers["Content-Type"]


# Validate the json schema of the response when making a patch request to the "posts" endpoint
def test_response_json_schema_validation():
    response = requests.patch("{}/1".format(posts_endpoint), json=posts_endpoint_patch_method_request_json)
    assert validate_posts_endpoint_response_json_schema(response.json())


# Validate the number of fields returned in the response when making a patch request to the "posts" endpoint
def test_number_of_items_returned():
    response = requests.patch("{}/1".format(posts_endpoint))
    assert len(response.json()) == 4

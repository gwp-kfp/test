import requests

from lib.aux import validate_posts_endpoint_response_json_schema
from lib.constants import posts_endpoint, posts_endpoint_post_method_request_json


# Validate the status code of the response when making post request to the "posts" endpoint is 201
def test_response_status_code_is_201():
    response = requests.post("{}".format(posts_endpoint))
    print(response.json())
    assert response.status_code == 201


# Validate the content type of the response when making post request to the "posts" endpoint is json
def test_response_content_type_is_json():
    response = requests.post("{}".format(posts_endpoint))
    assert "application/json" in response.headers["Content-Type"]


# Validate the json schema of the response when making a post request to the "posts" endpoint
def test_response_json_schema_validation():
    response = requests.post("{}".format(posts_endpoint), json=posts_endpoint_post_method_request_json)
    assert validate_posts_endpoint_response_json_schema(response.json())


# Validate the number of fields returned in the response when making a post request to the "posts" endpoint
def test_number_of_items_returned():
    response = requests.post("{}".format(posts_endpoint))
    assert len(response.json()) == 1

import requests

from lib.aux import validate_users_endpoint_response_json_schema
from lib.constants import users_endpoint


# Validate the status code of the response when making get request to the "users" endpoint is 200
def test_response_status_code_is_200():
    response = requests.get(users_endpoint)
    assert response.status_code == 200


# Validate the status code of the response when retrieving a valid user is 200
def test_valid_user_response_status_code_is_200():
    response = requests.get("{}/1".format(users_endpoint))
    assert response.status_code == 200


# Validate the status code of the response when retrieving a non-existent user is 404
def test_invalid_user_response_status_code_is_404():
    response = requests.get("{}/100".format(users_endpoint))
    assert response.status_code == 404


# Validate the content type of the response when making get request to the "users" endpoint is json
def test_response_content_type_is_json():
    response = requests.get(users_endpoint)
    assert "application/json" in response.headers["Content-Type"]


# Validate the json schema of the response when making a get request to the "users" endpoint
def test_response_json_schema_validation():
    response = requests.get(users_endpoint)
    assert validate_users_endpoint_response_json_schema(response.json())


# Validate the total number of users returned in the response when making a get request to the "users" endpoint
def test_number_of_users_returned():
    response = requests.get(users_endpoint)
    assert len(response.json()) == 10

import requests

from lib.aux import validate_users_endpoint_response_json_schema, validate_email_string, validate_website_string
from lib.constants import users_endpoint, users_endpoint_put_method_request_json


# Validate the status code of the response of put request to update a valid user is 200
def test_valid_user_response_status_code_is_200():
    response = requests.put("{}/1".format(users_endpoint))
    assert response.status_code == 200


# Validate the status code of the response of put request to update a non-existent user is 500
def test_invalid_user_response_status_code_is_500():
    response = requests.put("{}/100".format(users_endpoint))
    assert response.status_code == 500


# Validate the content type of the response when making put request to the "users" endpoint is json
def test_response_content_type_is_json():
    response = requests.put("{}/1".format(users_endpoint))
    assert "application/json" in response.headers["Content-Type"]


# Validate the json schema of the response when making a put request to the "users" endpoint
def test_response_json_schema_validation():
    response = requests.put("{}/1".format(users_endpoint), json=users_endpoint_put_method_request_json)
    assert validate_users_endpoint_response_json_schema(response.json())


# Validate the email format when making a put request to the "users" endpoint
def test_email_format_validation():
    response = requests.put("{}/1".format(users_endpoint), json=users_endpoint_put_method_request_json)
    assert validate_email_string(response.json()["email"])


# Validate the email format when making a put request to the "users" endpoint
def test_website_format_validation():
    response = requests.put("{}/1".format(users_endpoint), json=users_endpoint_put_method_request_json)
    assert validate_website_string(response.json()["website"])


# Validate the number of fields returned in the response when making a put request to the "users" endpoint
def test_number_of_items_returned():
    response = requests.put("{}/1".format(users_endpoint))
    assert len(response.json()) == 1

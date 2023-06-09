import jsonschema
import re

from lib.constants import expected_user_json_schema, expected_post_json_schema


def validate_json_schema(actual_schema, expected_schema):
    try:
        if type(actual_schema) == list:
            for item in actual_schema:
                jsonschema.validate(item, expected_schema)
        elif type(actual_schema) == dict:
            jsonschema.validate(actual_schema, expected_schema)
    except jsonschema.exceptions.ValidationError as ex:
        print(ex)
        return False
    return True


def validate_users_endpoint_response_json_schema(json_schema):
    return validate_json_schema(json_schema, expected_user_json_schema)


def validate_posts_endpoint_response_json_schema(json_schema):
    return validate_json_schema(json_schema, expected_post_json_schema)


def validate_email_string(email):
    return bool(re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email))


def validate_website_string(website):
    return bool(re.fullmatch(r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})'
                             r'|([a-zA-Z0-9][a-zA-Z0-9-_]{1,61}[a-zA-Z0-9]))\.([a-zA-Z]{2,6}|[a-zA-Z0-9-]{2,30}\.'
                             r'[a-zA-Z]{2,3})$', website))

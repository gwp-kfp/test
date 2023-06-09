base_url = "https://jsonplaceholder.typicode.com"
users_endpoint = "{}/users".format(base_url)
posts_endpoint = "{}/posts".format(base_url)

expected_user_json_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "username": {"type": "string"},
            "email": {"type": "string"},
            "address": {"type": "object"},
            "phone": {"type": "string"},
            "website": {"type": "string"},
            "company": {"type": "object"},
        },
        "required": ["id", "name", "username", "email", "address", "phone", "website", "company"],
        "additionalProperties": False
    }

expected_post_json_schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"},
        },
        "required": ["userId", "id", "title", "body"],
        "additionalProperties": False
    }

users_endpoint_post_method_request_json = {
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets"
    }
}

users_endpoint_put_method_request_json = {
    "id": 11,
    "name": "New User",
    "username": "None",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets"
    }
}

users_endpoint_patch_method_request_json = {
        "id": 11,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz"
    }

posts_endpoint_post_method_request_json = {
    "userId": 1,
    "title": "test title",
    "body": "test body"
}

posts_endpoint_put_method_request_json = {
    "userId": 1,
    "id": 101,
    "title": "put test title",
    "body": "put test body"
}

posts_endpoint_patch_method_request_json = {
    "userId": 1,
    "id": 101,
    "title": "patch test title",
}

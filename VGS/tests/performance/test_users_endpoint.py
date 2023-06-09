from locust import SequentialTaskSet, HttpUser, task, constant

from lib.constants import users_endpoint, users_endpoint_post_method_request_json, \
    users_endpoint_put_method_request_json, users_endpoint_patch_method_request_json


class UsersEndpoint(SequentialTaskSet):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.userId = None

    @task
    def post_request_to_users_endpoint(self):
        response = self.client.post("", json=users_endpoint_post_method_request_json)
        self.userId = response.json()["id"]

    @task
    def get_request_to_users_endpoint_after_post(self):
        self.client.get("/{}".format(self.userId))


    @task
    def put_request_to_users_endpoint(self):
        self.client.put("/{}".format(self.userId), json=users_endpoint_put_method_request_json)

    @task
    def patch_request_to_users_endpoint(self):
        self.client.patch("/{}".format(self.userId), json=users_endpoint_patch_method_request_json)

    @task
    def delete_request_to_users_endpoint(self):
        self.client.delete("/{}".format(self.userId))

    @task
    def get_request_to_users_endpoint_after_delete(self):
        self.client.get("/{}".format(self.userId))


class Users(HttpUser):
    host = users_endpoint
    wait_time = constant(1)
    tasks = [UsersEndpoint]

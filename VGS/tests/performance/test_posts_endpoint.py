from locust import SequentialTaskSet, HttpUser, task, constant

from lib.constants import posts_endpoint, posts_endpoint_post_method_request_json, \
    posts_endpoint_put_method_request_json, posts_endpoint_patch_method_request_json


class PostsEndpoint(SequentialTaskSet):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.postId = None

    @task
    def post_request_to_posts_endpoint(self):
        response = self.client.post("", json=posts_endpoint_post_method_request_json)
        self.postId = response.json()["id"]

    @task
    def get_request_to_posts_endpoint_after_post(self):
        self.client.get("/{}".format(self.postId))


    @task
    def put_request_to_posts_endpoint(self):
        self.client.put("/{}".format(self.postId), json=posts_endpoint_put_method_request_json)

    @task
    def patch_request_to_posts_endpoint(self):
        self.client.patch("/{}".format(self.postId), json=posts_endpoint_patch_method_request_json)

    @task
    def delete_request_to_posts_endpoint(self):
        self.client.delete("/{}".format(self.postId))

    @task
    def get_request_to_posts_endpoint_after_delete(self):
        self.client.get("/{}".format(self.postId))


class Posts(HttpUser):
    host = posts_endpoint
    wait_time = constant(1)
    tasks = [PostsEndpoint]

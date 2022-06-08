import json

from locust import HttpUser, TaskSet, task


class UserBehavior(TaskSet):
    base_url = '/v1/users'

    @task(1)
    def create_user(self):
        self.client.post(f"{self.base_url}/create", json.dumps({
            "uuid": "123e4567-e89b-12d3-a456-426655440000",
            "email": "test@mail.ru"
        }))


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 5000
    max_wait = 9000

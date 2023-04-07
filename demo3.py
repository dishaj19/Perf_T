import random
from locust import HttpUser, TaskSet, task, between, SequentialTaskSet


class MyReq(SequentialTaskSet):
    @task
    def on_start(self):
        res1 = self.client.get('/')
        print("get method status is", res1.status_code)

        csrf_token = res1.cookies['csrftoken']
        res2 = self.client.post('/', {'username': 'admin', 'password': 'admdf'},
                                headers={'X-CSRFToken': csrf_token})

        #  res1 = self.client.post('/', {"username": 'admin', "password": 'admin'})
        res2.raise_for_status()
        print("status of login page", res2.status_code)
        # print(f"DEBUG: login response.status_code = {res2.status_code}")

        # login done or not


    @task
    def index(self):
        res3 = self.client.get("/#/airnets")
        print("status of home page", res3.status_code)


class MySeq(HttpUser):
    wait_time = between(1, 10)
    host = "http://10.91.28.85"
    tasks = [MyReq]

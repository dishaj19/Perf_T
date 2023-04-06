
from locust import HttpUser, task, TaskSet, SequentialTaskSet, constant, between
import time
import locust


class MyReq(SequentialTaskSet):
    def on_start(self):
        self.login()

    @task
    def login(self):
        start = time.time()
        response1 = self.client.get('/')
        print("get method status is", response1.status_code)
        csrf_token = response1.cookies['csrftoken']
        response2 = self.client.post('/', {'username': 'admin', 'password': 'adm12'},
                                     headers={'X-CSRFToken': csrf_token})
        end = time.time()
        print("post method status is", response2.status_code)
        print(f"DEBUG: login response.status_code = {response2.status_code}")
        # after logging status code
        print("starting time ", start)
        print("ending time ", end)
        print("total time= ", (end - start))

        with self.client.get("/#/airnets", catch_response=True) as response:
            if response.data == "fail":
                raise ResponseError("Request failed")

        res3 = self.client.option()
        # response3 = self.client.get('http://10.91.28.85/#/airnets')
        # print("get method for airnet page status is", response3.status_code)


class MySeq(HttpUser):
    wait_time = between(1, 5)
    host = "http://10.91.28.85"
    tasks = [MyReq]

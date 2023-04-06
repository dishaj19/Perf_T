from locust import HttpUser, task, TaskSet, SequentialTaskSet, constant, between
import time
from openpyxl import workbook, load_workbook

class MyReq(SequentialTaskSet):
    def on_start(self):
        self.login()

    @task
    def login(self):
        i = 1
        j = 1
        for i in range(1, 11, 1):
            response1 = self.client.get('/')
            print("get method status is", response1.status_code)
            start = time.time()
            csrf_token = response1.cookies['csrftoken']
            response2 = self.client.post('/', {'username': i, 'password': j},
                                         headers={'X-CSRFToken': csrf_token})
            end = time.time()
            print("post method status is", response2.status_code)
            print(f"DEBUG: login response.status_code = {response2.status_code}")
            # after logging status code
            print(end - start)
            print({"username": i})


class MySeq(HttpUser):
    wait_time = between(1, 5)
    host = "http://10.91.28.85"
    tasks = [MyReq]


book_wb = load_workbook('scenario2ID1111.xlsx')
sheet = book_wb.active
# print(sheet['A1'].value)




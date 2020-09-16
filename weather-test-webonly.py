import random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def index_page(self):
        self.client.verify = False
        self.client.get("/", verify=False)
        self.client.get("/about", verify=False)
        self.client.get("/weather/Canberra", verify=False)

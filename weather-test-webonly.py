import random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)
    def on_start(self):
        self.client.verify = False

    @task
    def index_page(self):
        self.client.get("/", verify=False)
        self.client.get("/about", verify=False)
        self.client.get("/weather/Canberra", verify=False)

import random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def index_page(self):
        self.client.get(verify=False, "/")
        self.client.get(verify=False, "/about")
        self.client.get(verify=False, "/weather/Canberra")

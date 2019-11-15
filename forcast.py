from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        self.client.get("/")

    def logout(self):
        self.client.get("/")

    @task(1)
    def profile(self):
        self.client.get('/api?latitude=-35.2819&longitude=149.1289&location="Canberra, Australian Capital Territory"')

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

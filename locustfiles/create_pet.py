import random
from locust import HttpUser, task, between
from helpers import random_string, check_response, load_test_data, THINK_TIME_MIN, THINK_TIME_MAX

class CreatePetUser(HttpUser):
    wait_time = between(THINK_TIME_MIN, THINK_TIME_MAX)
    test_data = load_test_data()

    @task
    def create_pet(self):
        payload = {
            "name": f"pet_{random_string(5)}",
            "status": random.choice(self.test_data['petStatuses']),
            "category": random.choice(self.test_data['categories'])
        }

        with self.client.post("/pet", json=payload, catch_response=True) as response:
            try:
                check_response(response)
                response.success()
            except AssertionError as e:
                response.failure(str(e))

    def on_start(self):
        # Verify the API is accessible
        response = self.client.get("/")
        if response.status_code != 200:
            print(f"Warning: API returned status code {response.status_code}")
import random
from locust import HttpUser, task, between
from helpers import (
    check_response,
    THINK_TIME_MIN,
    THINK_TIME_MAX,
    PET_ENDPOINT,
    verify_api_availability
)

class GetPetUser(HttpUser):
    wait_time = between(THINK_TIME_MIN, THINK_TIME_MAX)

    @task
    def get_pet(self):
        pet_id = random.randint(1, 10)  # Assuming pets with IDs 1-10 exist
        with self.client.get(f"{PET_ENDPOINT}/{pet_id}", catch_response=True) as response:
            try:
                check_response(response)
                response.success()
            except AssertionError as e:
                response.failure(str(e))

    def on_start(self):
        verify_api_availability()
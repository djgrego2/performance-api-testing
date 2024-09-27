import random
import string
import json
import requests
from helpers.constants import BASE_URL

def random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def load_test_data():
    with open('data/test_data.json', 'r') as file:
        return json.load(file)

def check_response(response):
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.json(), "Empty response body"

def verify_api_availability():
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            print("API is accessible.")
        else:
            print(f"Warning: API returned status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Error accessing API: {e}")
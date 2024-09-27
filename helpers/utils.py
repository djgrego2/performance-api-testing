import random
import string
import json

def random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def load_test_data():
    with open('data/test_data.json', 'r') as file:
        return json.load(file)

def check_response(response):
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.json(), "Empty response body"
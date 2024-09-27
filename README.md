# Gregorio Challenge - Petstore API Performance Testing with Locust

## Description
This project contains performance tests for the Petstore API using Locust, a modern, Python-based load testing tool. It demonstrates best practices in API performance testing and provides a scalable structure for building and running performance tests.

## Technologies Used
- Python 3.8+
- Locust
- Requests

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Project Setup
1. Clone the repository:
   ```
   git clone https://github.com/your-username/petstore-performance-testing.git
   ```
2. Navigate to the project directory:
   ```
   cd petstore-performance-testing
   ```
3. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Project Structure
```
performance-api-test/
├── locustfiles/
│   ├── create_pet.py
│   ├── get_pet.py
│   ├── update_pet.py
├── helpers/
│   ├── __init__.py
│   ├── utils.py
│   └── constants.py
├── data/
│   └── test_data.json
├── config.py
├── requirements.txt
└── README.md
```

- `locustfiles/`: Contains Locust test files
- `helpers/`: Reusable functions and constants
- `data/`: Test data files
- `config.py`: Configuration for test environments

## Running Tests
To run a specific test scenario:
```
locust -f locustfiles/create_pet.py --host=http://localhost:8080/api/v3
```

Then, open a web browser and go to http://localhost:8089 to start the test.

Note: Make sure your Petstore API is running at http://localhost:8080/api/v3 before starting the tests.

## Test Scenarios
- `create_pet.py`: Tests the performance of creating new pets
- `get_pet.py`: Tests the performance of retrieving pet information
- `update_pet.py`: Tests the performance of updating existing pets

## Verifying API Availability
Before running the tests, you can verify if the API is accessible:

```python
from helpers.utils import verify_api_availability

verify_api_availability()
```

This will attempt to connect to the API and print the status.

## Environment Variables
You can set the following environment variables to configure the tests:

- `TEST_ENV`: Set the test environment (DEFAULT, DEV, STAGING, PROD). If not set, it defaults to 'DEFAULT'.

Example:
```
TEST_ENV=DEV locust -f locustfiles/create_pet.py
```

This will use the configuration defined for the DEV environment in `config.py`.

## Best Practices
1. **Modularization**: Tests are organized into separate files for better maintainability.
2. **Configuration Management**: Use `config.py` to manage different environments.
3. **Parameterization**: Utilize `data/test_data.json` for dynamic test data.
4. **Error Handling**: Implement proper error handling and logging.
5. **Custom Metrics**: Use Locust's custom metrics for detailed performance insights.

## Customizing Tests
To create new test scenarios or modify existing ones:

1. Create a new file in the `locustfiles/` directory or modify an existing one.
2. Define a new `HttpUser` class with tasks that represent user behavior.
3. Use the `@task` decorator to define the relative weight of different tasks.
4. Utilize helpers from the `helpers/` package for common operations.

Example:
```python
from locust import HttpUser, task, between
from helpers import check_response, PET_ENDPOINT

class MyCustomUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def my_custom_task(self):
        with self.client.get(f"{PET_ENDPOINT}/1", catch_response=True) as response:
            check_response(response)
```

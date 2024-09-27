import os
class Config:
    DEFAULT = {
        'base_url': 'http://localhost:8080/api/v3',
        'think_time_min': 1,
        'think_time_max': 3
    }
    DEV = DEFAULT.copy()
    STAGING = DEFAULT.copy()
    PROD = DEFAULT.copy()

    @staticmethod
    def get_config():
        env = os.getenv('TEST_ENV', 'DEFAULT')
        return getattr(Config, env)
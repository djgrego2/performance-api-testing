from config import Config

current_config = Config.get_config()

BASE_URL = current_config['base_url']
THINK_TIME_MIN = current_config['think_time_min']
THINK_TIME_MAX = current_config['think_time_max']

# API endpoints
PET_ENDPOINT = "/pet"
STORE_ENDPOINT = "/store"
USER_ENDPOINT = "/user"
import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")


def get_count(country, role):
    url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/1"
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": role,
        "results_per_page": 1,
    }
    response = requests.get(url, params=params)
    return response.json()["count"]


print(get_count("es", "junior frontend"))
print(get_count("nl", "junior frontend"))
print(get_count("de", "junior frontend"))
print(get_count("be", "junior frontend"))

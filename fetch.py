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
        "title_only": role,
        "results_per_page": 1,
    }
    response = requests.get(url, params=params)
    return response.json()["count"]


def show_title(country, role):
    url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/1"
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "title_only": role,
        "results_per_page": 10,
    }
    response = requests.get(url, params=params)
    jobs = response.json()["results"]

    for job in jobs:
        print(job["title"])


COUNTRIES = ["es", "nl", "de", "be"]
ROLES = {
    "frontend": ["front end", "frontend", "Frontend-Entwickler", "Desarrollador Front"],
    "backend": ["back end", "backend", "Backend-Entwickler", "Desarrollador Backend"],
    "full stack": ["full stack", "fullstack"],
    "ux": ["ux & ui", "UX/UI"],
    "software developer": ["software developer", "software engineer", "desarrollo de software"],
    "web developer": ["web developer", "desarrollador web", "Webentwickler"],
    "mobile developer": ["mobile developer", "react native"]
}

# for country in COUNTRIES:
show_title("nl", "mobile developer")
#    for role, terms in ROLES.items():
#        total = 0
#        for term in terms:
#            total = total + get_count(country, term)
#        print(f"{country} | {role}: {total}")

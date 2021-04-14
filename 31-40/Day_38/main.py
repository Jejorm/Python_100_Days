import requests
from datetime import datetime
from os import environ

APP_ID = environ.get("NUTR_APP_ID")
API_KEY = environ.get("NUTR_API_KEY")
GENDER = environ.get("GENDER")
WEIGHT_KG = environ.get("WEIGHT")
HEIGHT_CM = environ.get("HEIGHT")
AGE = environ.get("AGE")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
user_prompt = input("Tell me which exercises you did: ")

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
exercise_params = {
    "query": user_prompt,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, headers=exercise_headers, json=exercise_params)
result = response.json()

today = datetime.now()
today_formatted = today.strftime("%d/%m/%Y")
time_formatted = today.strftime("%X")

sheety_endpoint = environ.get("SHEETY_ENDPOINT")
sheety_headers = {
    "Authorization": f"Basic {environ.get('SHEETY_AUTH')}",
}

for exercise in result["exercises"]:
    sheety_params = {
        "workout":
            {
                "date": today_formatted,
                "time": time_formatted,
                "exercise": exercise["name"].title(),
                "duration": int(exercise["duration_min"]),
                "calories": exercise["nf_calories"],
            },
    }

    sheety_response = requests.post(sheety_endpoint, headers=sheety_headers, json=sheety_params)

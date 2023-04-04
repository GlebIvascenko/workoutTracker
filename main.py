import requests
from datetime import datetime

APP_ID = "7ab0e5eb"
API_KEY = "624d54747ec28996c0f6a53f37b40d87"

USERNAME = "c82db584a9e2af7b490db5017784195b"
PROJECT_NAME = 'myWorkoutTracker'
SHEET_NAME = "workouts"


tracker_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}
bearer_headers = {
    'Authorization': "Bearer dsfidbiuhUHKMGGMFDKSFSYGMKLlmgygsdklufhvmlvn32m4fmdufhmei2",
}



tracker_config = {
 "query": input("Tell me about your exercise: "),
 "gender": "male",
 "weight_kg": 91.1,
 "height_cm": 178,
 "age": 29
}


response = requests.post(url=tracker_endpoint, json=tracker_config, headers=headers)
plan = response.json()

today = datetime.now()

for exercise in plan['exercises']:
    workout_did = {
        "workout": {
            "date": today.strftime("%m/%d/%Y"),
            "time": today.strftime('%X'),
            "exercise": exercise["name"].title(),
            "duration": f"{exercise['duration_min']}min",
            "calories": exercise['nf_calories'],
        }
    }

    response = requests.post(url=sheety_endpoint, json=workout_did, headers=bearer_headers)

    print(response.text)
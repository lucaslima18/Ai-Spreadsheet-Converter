import json, requests
from settings import *


def postExample(text, intent):
    url = "https://api.bothub.it/v2/repository/example/"
    data = {
            "repository": REPOSITORY_UUID,
            "text": text,
            "intent": intent,
            "language": LANGUAGE,
            "entities": []
        }
    headers = {
                'Content-Type': 'application/json',
                'Authorization': AUTH_TOKEN
            }
    print(f"{requests.post(url, data=json.dumps(data), headers=headers)}\n")

def postTests(text, intent):
    url = "https://api.bothub.it/v2/repository/evaluate/"
    data = {
            "repository": REPOSITORY_UUID,
            "text": text,
            "intent": intent,
            "language": LANGUAGE,
            "entities": []
        }
    headers = {
                'Content-Type': 'application/json',
                'Authorization': AUTH_TOKEN
            }
    print(f"{requests.post(url, data=json.dumps(data), headers=headers)}\n")





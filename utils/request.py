# Required Libraries
import requests
import json

from settings.config import Settings

# Base URL
url = 'https://api.imeicheck.net/v1/checks'


# Execute request
def get_request(token: str, device_id: str):
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    body = json.dumps({
        "deviceId": f"{device_id}",
        "serviceId": 1
    })
    response = requests.post(url, headers=headers, data=body)
    return response

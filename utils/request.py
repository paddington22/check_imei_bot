# Required Libraries
import requests
import json

from settings.config import Settings

# Base URL
url = 'https://api.imeicheck.net/v1/checks'

token = Settings.API_TOKEN

# Add necessary headers
headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}


# Execute request
def get_request(device_id):
    body = json.dumps({
        "deviceId": f"{device_id}",
        "serviceId": 1
    })
    response = requests.post(url, headers=headers, data=body)
    return response

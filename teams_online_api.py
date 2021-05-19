import requests
import time
from requests.auth import HTTPBasicAuth

header = {
    'X-Auth-Token':'BBFF-umsbNa5Ha9COz6W4KxTNDRcB4ei8KG',
    'CONTENT-TYPE':'application/json'
}

BASE_URL = "https://login.microsoftonline.com/8ff744c5-302b-412b-9679-38385b4f1e3b/oauth2/v2.0"
PATH = "/token/"

myjson = {
    'client_id': 1231,
    'variable2':1211
}

def getAccessToken():
    BASE_URL = "https://login.microsoftonline.com/8ff744c5-302b-412b-9679-38385b4f1e3b/oauth2/v2.0"
    PATH = "/token/"
    x = requests.post(BASE_URL+PATH , headers = header)
    json_response = x.json()

    print(json_response)


getAccessToken()

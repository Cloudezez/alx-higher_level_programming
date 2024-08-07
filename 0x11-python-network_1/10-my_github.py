#!/usr/bin/python3
import sys
import requests
from requests.auth import HTTPBasicAuth

username = sys.argv[1]
token = sys.argv[2]
url = "https://api.github.com/user"
response = requests.get(url, auth=HTTPBasicAuth(username, token))

try:
    print(response.json().get('id'))
except ValueError:
    print(None)


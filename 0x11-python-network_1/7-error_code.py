#!/usr/bin/python3
import sys
import requests

url = sys.argv[1]
response = requests.get(url)
if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
else:
    print(response.text)


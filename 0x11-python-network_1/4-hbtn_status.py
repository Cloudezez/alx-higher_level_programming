#!/usr/bin/python3
import requests

url = "https://alx-intranet.hbtn.io/status"
response = requests.get(url)
body = response.text
print("Body response:")
print(f"    - type: {type(body)}")
print(f"    - content: {body}")


#!/usr/bin/python3
import sys
import requests

q = sys.argv[1] if len(sys.argv) > 1 else ""
url = "http://0.0.0.0:5000/search_user"
response = requests.post(url, data={'q': q})

try:
    data = response.json()
    if not data:
        print("No result")
    else:
        print(f"[{data['id']}] {data['name']}")
except ValueError:
    print("Not a valid JSON")


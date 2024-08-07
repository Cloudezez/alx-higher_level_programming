#!/usr/bin/python3
import sys
import requests

url = sys.argv[1]
response = requests.get(url)
print(response.headers.get('X-Request-Id'))


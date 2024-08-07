#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

if len(sys.argv) != 3:
    print("Usage: ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]
data = urllib.parse.urlencode({'email': email}).encode('ascii')

try:
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code:", e.code)


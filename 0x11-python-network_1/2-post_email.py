#!/usr/bin/python3
import sys
from urllib import request, parse

url = sys.argv[1]
email = sys.argv[2]
data = parse.urlencode({'email': email}).encode('utf-8')
req = request.Request(url, data=data)
with request.urlopen(req) as response:
    body = response.read().decode('utf-8')
    print(body)


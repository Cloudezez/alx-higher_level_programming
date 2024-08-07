#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib and prints details
about the response.
"""

import urllib.request

def main():
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    main()


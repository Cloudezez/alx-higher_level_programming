#!/usr/bin/python3
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    token = sys.argv[2]
    
    # Print to verify the arguments are correct
    print(f"Username: {username}")
    print(f"Token: {token}")

    # Define the URL for the GitHub API
    url = "https://api.github.com/user"
    
    # Make the GET request with Basic Authentication
    response = requests.get(url, auth=HTTPBasicAuth(username, token))
    
    # Print the JSON response and status code
    print(response.json())
    print(response.status_code)


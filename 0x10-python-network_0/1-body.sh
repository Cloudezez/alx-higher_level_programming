#!/bin/bash
# Send a GET request to the URL and display the body if the status code is 200

# Store the HTTP response code in a variable
response_code=$(curl -s -o response.txt -w "%{http_code}" "$1")

# Output the response code for debugging
echo "Status Code: $response_code"

# Check if the response code is 200
if [ "$response_code" -eq 200 ]; then
  # If the status code is 200, display the body of the response
  cat response.txt
fi


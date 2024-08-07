#!/bin/bash
# Sends a GET request to the URL and displays the body of a 200 status code response
status_code=$(curl -sL -o /dev/null -w "%{http_code}" "$1")
echo "Status code: $status_code"
if [ "$status_code" -eq 200 ]; then
    curl -sL "$1"
fi


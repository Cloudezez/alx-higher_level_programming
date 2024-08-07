#!/bin/bash
# Sends a GET request to the URL and displays the body of a 200 status code response
if [ "$(curl -sL -w "%{http_code}" -o /dev/null "$1")" -eq 200 ]; then curl -sL "$1"; fi

#!/bin/bash
# Get the size of the body of the response from the URL
curl -s "$1" | wc -c


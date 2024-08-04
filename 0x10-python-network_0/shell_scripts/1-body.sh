#!/bin/bash
# Script to display the body of a 200 status code response

curl -s "$1" | grep -i "200 OK"


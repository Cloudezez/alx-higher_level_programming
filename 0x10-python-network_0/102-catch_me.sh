#!/bin/bash
# Makes a request to the catch_me endpoint
curl -s -X PUT -H "Origin: School" -d "user_id=98" "$1"

#!/bin/bash
# Script to display the size of the body of a response

curl -sI "$1" | grep -i Content-Length | awk '{print $2}'


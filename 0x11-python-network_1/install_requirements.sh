#!/bin/bash

# Update package list and install pip if not already installed
sudo apt update
sudo apt install -y python3-pip

# Install Flask
pip3 install Flask

# Install other required packages
pip3 install requests


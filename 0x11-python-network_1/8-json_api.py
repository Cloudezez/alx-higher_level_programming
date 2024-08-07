#!/usr/bin/python3
import sys
import requests


def main():
    """Main function to handle API requests and response processing."""
    
    # Get the letter from command-line arguments, default to an empty string
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Define the URL for the API request
    url = "http://0.0.0.0:5000/search_user"

    # Make the POST request with the letter as a parameter
    response = requests.post(url, data={'q': q})

    try:
        # Attempt to parse the JSON response
        json_response = response.json()

        if json_response:
            # If JSON is valid and not empty, print the id and name
            print(f"[{json_response['id']}] {json_response['name']}")
        else:
            # JSON is empty
            print("No result")
    except ValueError:
        # Handle case where response is not valid JSON
        print("Not a valid JSON")


if __name__ == "__main__":
    main()


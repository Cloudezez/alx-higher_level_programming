ALX Higher Level Programming - Python Network 1
This repository contains Python scripts for various networking tasks using both urllib and requests libraries. The tasks include fetching status, handling headers, posting data, and handling HTTP errors.

Directory Structure
The project directory 0x11-python-network_1 contains the following scripts:

Scripts
0-hbtn_status.py

Fetches https://alx-intranet.hbtn.io/status and displays the type, content, and UTF-8 content of the response.
1-hbtn_header.py

Takes a URL as an argument, sends a request to the URL, and displays the value of the X-Request-Id variable found in the response header.
2-post_email.py

Takes a URL and an email address as arguments, sends a POST request to the URL with the email as a parameter, and displays the body of the response (decoded in UTF-8).
3-error_code.py

Takes a URL as an argument, sends a request to the URL, and displays the body of the response. Manages HTTP errors and prints the error code if an exception is raised.
4-hbtn_status.py

Fetches https://alx-intranet.hbtn.io/status using requests and displays the type and content of the response.
5-hbtn_header.py

Takes a URL as an argument, sends a request to the URL using requests, and displays the value of the X-Request-Id variable found in the response header.
6-post_email.py

Takes a URL and an email address as arguments, sends a POST request to the URL with the email as a parameter using requests, and displays the body of the response.
7-error_code.py

Takes a URL as an argument, sends a request to the URL using requests, and displays the body of the response. If the HTTP status code is greater than or equal to 400, prints the error code.
8-json_api.py

Takes a letter as an argument, sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter, and displays the ID and name if the response is a valid JSON. Handles cases where the JSON is empty or invalid.
10-my_github.py

Takes GitHub credentials (username and personal access token) and uses the GitHub API to display the user ID.
Requirements
Python version: 3.8.5
Packages:
urllib (for scripts using urllib)
requests (for scripts using requests)
Running the Scripts
Make sure each script has executable permissions:

bash
Copy code
chmod +x <script_name>.py
You can run each script from the command line as follows:

bash
Copy code
./<script_name>.py [arguments]
Replace [arguments] with the required arguments for each script. For example:

bash
Copy code
./1-hbtn_header.py https://alx-intranet.hbtn.io
Testing
Test each script in the provided sandbox or environment to ensure it meets the expected output.

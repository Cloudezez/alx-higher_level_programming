# 0x10-python-network_0

This project contains various Bash scripts for making HTTP requests using `curl`, as well as a Python script to find a peak in a list of unsorted integers.

## Requirements

- All Bash scripts are exactly 3 lines long.
- All Python files conform to PEP 8 style guide.
- Scripts are tested on Ubuntu 20.04 LTS.

## Tasks

### 0. cURL body size

- **Script:** `0-body_size.sh`
- **Usage:** `./0-body_size.sh <URL>`
- **Description:** Sends a request to the URL and displays the size of the response body in bytes.

### 1. cURL to the end

- **Script:** `1-body.sh`
- **Usage:** `./1-body.sh <URL>`
- **Description:** Sends a GET request to the URL and displays the body of the response, but only if the response status code is 200.

### 2. cURL Method

- **Script:** `2-delete.sh`
- **Usage:** `./2-delete.sh <URL>`
- **Description:** Sends a DELETE request to the URL and displays the body of the response.

### 3. cURL only methods

- **Script:** `3-methods.sh`
- **Usage:** `./3-methods.sh <URL>`
- **Description:** Displays all HTTP methods the server will accept.

### 4. cURL headers

- **Script:** `4-header.sh`
- **Usage:** `./4-header.sh <URL>`
- **Description:** Sends a GET request to the URL with a custom header variable `X-School-User-Id: 98` and displays the body of the response.

### 5. cURL POST parameters

- **Script:** `5-post_params.sh`
- **Usage:** `./5-post_params.sh <URL>`
- **Description:** Sends a POST request to the URL with the variables `email=test@gmail.com` and `subject=I will always be here for PLD`.

### 6. Find a peak

- **Script:** `6-peak.py`, `6-main.py`, `6-peak.txt`
- **Usage:** `./6-main.py`
- **Description:** A Python script to find a peak in a list of unsorted integers. `6-peak.txt` contains the complexity analysis.


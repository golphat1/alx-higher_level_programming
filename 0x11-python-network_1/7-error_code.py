#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
use the packages requests and sys
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        print(response.text)
    except requests.exceptions.RequestException as e:
        if hasattr(e, 'response') and e.response is not None:
            print("Error code:", e.response.status_code)
        else:
            print("Error:", e)

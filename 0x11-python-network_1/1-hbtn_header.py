#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable
found in the header of the response.
use the packages urllib and sys.
"""
import urllib.request
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
                print(x_request_id)
    except urllib.error.URLError as e:
        print("Error fetching URL:", e)

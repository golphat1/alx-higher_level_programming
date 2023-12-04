#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
Manage urllib.error.HTTPError exceptions and
print: Error code: followed by the HTTP status code.
use the packages urllib and sys
"""
import sys
from urllib import request, error


def fetch_url_content(url):
    try:
        with request.urlopen(url) as response:
            return response.read().decode('UTF-8')
    except error.HTTPError as e:
        return f'Error code: {e.code}'


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    content = fetch_url_content(url)
    print(content)

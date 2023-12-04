#!/usr/bin/python3
"""
Takes in a URL and an email address, sends a POST request
to the passed URL with the email as a
parameter, and finally displays the body of the response.
The email must be sent in the variable email
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    try:
        response = requests.post(url, data=data)
        print("Your email is:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

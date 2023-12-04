#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
Use Basic Authentication with a personal access token as password to
access to your information (only read:user permission is needed).
The first argument will be your username
The second argument will be your password
Use the package requests and sys
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))
        if response.status_code == 200:
            data = response.json()
            print(data['id'])
        else:
            print(None)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

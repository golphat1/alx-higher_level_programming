#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    data = {'q': q}

    try:
        response = requests.post("http://0.0.0.0:5000/search_user", data=data)
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

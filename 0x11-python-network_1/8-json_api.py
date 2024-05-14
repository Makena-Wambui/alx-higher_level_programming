#!/usr/bin/python3

"""
Write a Python script that takes in a letter,
and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys.
"""

import requests
import sys

if __name__ == "__main__":

    arg = "" if len(sys.argv) == 1 else sys.argv[1]

    data = {'q': arg}
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        response = response.json()

        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get('id'), response.get('name')))
    except JSONDecodeError:
        print("Not a valid JSON")

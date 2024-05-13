#!/usr/bin/python3

"""
This module fetches https://alx-intranet.hbtn.io/status

You must use the package requests.
"""

import requests


if __name__ == "__main__":
    # our response object, r
    r = requests.get('https://alx-intranet.hbtn.io/status')

    # to read the contents of the server's response:
    response = r.text

    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))

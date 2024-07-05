#!/usr/bin/python3

"""
This module contains a Python script that
fetches https://alx-intranet.hbtn.io/status url.
"""

import urllib.request


if __name__ == "__main__":
    # first create a Request object; this represents the HTTP Request
    # you are making or the URL you want to fetch.
    request = urllib.request.Request(" https://alx-intranet.hbtn.io/status")
    # returns a response obj for this url, which is a file like object.
    with urllib.request.urlopen(request) as response:
        response = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode("utf-8")))

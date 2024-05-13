#!/usr/bin/python3

"""
This module takes in a URL,
sends a request to the URL and
displays the body of the response (decoded in utf-8).

You have to manage urllib.error.HTTPError exceptions,
and print: Error code: followed by the HTTP status code.
You must use the packages urllib and sys
You are not allow to import packages other than urllib and sys.
You must use a with statement.
"""

import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    # create a Request object
    request = urllib.request.Request(url)

    # call urlopen on request
    try:
        with urllib.request.urlopen(request) as response:
            response = response.read()
            response = response.decode("utf-8")
            print(response)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

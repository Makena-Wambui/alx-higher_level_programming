#!/usr/bin/python3

"""
This module takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

You must use the packages urllib and sys
You are not allow to import packages other than urllib and sys.
You must use a with statement.
"""

import sys
import urllib.request


url = sys.argv[1]

# create a Request object
request = urllib.request.Request(url)

# call urlopen on request
with urllib.request.urlopen(request) as response:
    # access the response headers.
    # use dict to convert into a dictionary object.
    # use get to extract the value of the X-Request-Id key.
    print(dict(response.headers).get("X-Request-Id"))

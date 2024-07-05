#!/usr/bin/python3

"""
This module takes in a URL, and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
The email must be sent in the email variable.

You must use the packages urllib and sys
You are not allow to import packages other than urllib and sys.
You must use a with statement.
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]  # Get the email from the command line arguments

    # Create a dictionary with the email parameter
    data = {"email": email}
    data_encoded = urllib.parse.urlencode(data).encode("utf-8")

    # Create a Request object with the POST method
    request = urllib.request.Request(url, data=data_encoded, method="POST")

    # Call urlopen on the request and handle the response
    with urllib.request.urlopen(request) as response:
        # Read and decode the response body
        response_body = response.read().decode("utf-8")
        print(response_body)

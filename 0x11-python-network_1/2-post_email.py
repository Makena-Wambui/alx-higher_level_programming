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

if __name__ == "__main__":
    url = sys.argv[1]

    # Create a Request object
    request = urllib.request.Request(url)

    # Call urlopen on the request and handle the response
    with urllib.request.urlopen(request) as response:
        # Get all headers from the response
        headers = response.getheaders()

        # Extract the X-Request-Id header
        for header in headers:
            if header[0].lower() == 'x-request-id':
                print(header[1])
                break

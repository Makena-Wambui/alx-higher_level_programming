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
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    email_val = sys.argv[2]
    email = {"email": "email_val"}

    # first encode the email using the urlencode function
    email = urllib.parse.urlencode(email)
    data = email.encode("ascii")

    # create a Request object, pass the email/data as a param.
    request = urllib.request.Request(url, data)

    # call urlopen on request
    try:
        with urllib.request.urlopen(request) as response:
            response = response.read()
            response = response.decode("utf-8")
            print(response)
    except urllib.error.URLError:
        pass

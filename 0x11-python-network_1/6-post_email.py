#!/usr/bin/python3

"""
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response.

The email must be sent in the variable email
You must use the packages requests and sys.
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    email_val = sys.argv[2]
    data = {"email": email_val}

    r = requests.post(url, data)

    print(r.text)

#!/usr/bin/python3

"""
This module contains a script takes in a URL,
sends a request to the URL and displays the value of
the variable X-Request-Id in the response header.

You must use the packages requests and sys
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)

    value = r.headers.get("X-Request-Id")

    print(value)

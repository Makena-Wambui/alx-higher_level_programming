#!/usr/bin/python3

"""
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API.
Print all commits by: `<sha>: <author name>` (one by line)
Write a Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys.
"""
import requests
import sys


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    response = requests.get(url)

    try:
        r = response.json()

        for i in range(10):
            print("{}: {}".format(r[i].get("sha"),
                                  r[i].get("commit")
                                      .get("author").get("name")))
    except Exception:
        print("Not a valid JSON")

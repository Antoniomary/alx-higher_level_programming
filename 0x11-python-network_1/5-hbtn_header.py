#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL and displays the value of the
    X-Request-Id variable found in the header of the response.
"""
import requests
import sys


def get_head():
    """get the X-Request-Id header value from a response"""
    res = requests.get(sys.argv[1])
    if "X-Request-Id" in res.headers.keys():
        print(res.headers["X-Request-Id"])


if __name__ == "__main__":
    get_head()

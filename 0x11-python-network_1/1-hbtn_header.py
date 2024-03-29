#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL and displays the value of the
    X-Request-Id variable found in the header of the response.
"""
import urllib.request as request
import sys


def get_head():
    """get the X-Request-Id header value from a response2"""
    with request.urlopen(sys.argv[1]) as res:
        print(res.getheader("X-Request-Id"))


if __name__ == "__main__":
    get_head()

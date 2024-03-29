#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8).
"""
import urllib.request as request
import urllib.error as error
import sys


def get_response():
    """gets response from a url and handles error"""
    try:
        with request.urlopen(sys.argv[1]) as res:
            response = res.read()
            print(response.decode())
    except error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    get_response()

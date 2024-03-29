#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8).
"""
import requests
import sys


def get_response():
    """gets response from a url and handles error"""
    response = requests.get(sys.argv[1])
    if response.status_code < 400:
        print(response.text)
    else:
        print(f"Error code: {response.status_code}")


if __name__ == "__main__":
    get_response()

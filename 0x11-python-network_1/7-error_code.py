#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8).
"""
import requests
import sys


def get_response():
    """gets response from a url and handles error"""
    try:
        response = requests.get(sys.argv[1])
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    get_response()

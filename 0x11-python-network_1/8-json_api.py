#!/usr/bin/python3
"""
    takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter
    as a parameter.
"""
import requests
import sys


def search_api():
    """search an api"""
    arg = ""
    if len(sys.argv) > 1:
        arg = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    request = requests.post(url, data={'q': arg})
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        res = request.json()
        if res:
            print(f"[{res['id']}] {res['name']}")
        else:
            print("No result")
    else:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_api()

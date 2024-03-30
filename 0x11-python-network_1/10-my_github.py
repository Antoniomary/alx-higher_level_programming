#!/usr/bin/python3
"""
    takes your GitHub credentials (username and password) and
    uses the GitHub API to display your id
"""
import requests
import sys


def search_api():
    """search an api"""
    user, pwd = sys.argv[1], sys.argv[2]
    url = 'https://api.github.com/user'
    request = requests.get(url, headers={'Authorization': f'Bearer {pwd}'})

    if request.status_code == 200:
        res = request.json()
        print(res['id'])
    else:
        print(None)


if __name__ == "__main__":
    search_api()

#!/usr/bin/python3
"""
    module for a function called search_commits
"""
import requests
import sys


def search_commits():
    """list 10 commits (from the most recent to oldest)
       of a given repository
    """
    repo, owner = sys.argv[1], sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    request = requests.get(url)
    if request.status_code == 200:
        res = request.json()
        for i in range(len(res)):
            if i == 10:
                break
            print(f"{res[i]['sha']}: {res[i]['commit']['author']['name']}")
    else:
        print(None)


if __name__ == "__main__":
    search_commits()

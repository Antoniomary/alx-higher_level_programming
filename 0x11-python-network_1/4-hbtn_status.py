#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests


def get_stat():
    """fetches https://alx-intranet.hbtn.io/status and prints it"""
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("    - type:", type(response))
    print("    - content:", response.text)


if __name__ == "__main__":
    get_stat()

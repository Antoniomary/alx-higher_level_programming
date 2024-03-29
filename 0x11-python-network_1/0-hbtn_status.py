#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import urllib.request as request


def get_stat():
    """fetches https://alx-intranet.hbtn.io/status and prints it"""
    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        response = res.read()
        print("Body response:")
        print("\t- type:", type(response))
        print("\t- content:", response)
        print("\t- utf8 content:", response.decode('utf8'))


if __name__ == "__main__":
    get_stat()

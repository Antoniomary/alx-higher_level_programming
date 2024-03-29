#!/usr/bin/python3
"""
    takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter,
    and displays the body of the response
    (decoded in utf-8)
"""
import urllib.request as request
import urllib.parse as parse
import sys


def post_email():
    """posts an email to a URL"""
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({"email": email})
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print("Your email is:", response.read().decode())


if __name__ == "__main__":
    post_email()

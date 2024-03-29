#!/usr/bin/python3
"""
    takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter,
    and displays the body of the response
    (decoded in utf-8)
"""
import requests
import sys


def post_email():
    """posts an email to a URL"""
    url = sys.argv[1]
    email = sys.argv[2].encode()

    response = requests.post(url, email)
    print("Your email is:", response.text.decode())


if __name__ == "__main__":
    post_email()

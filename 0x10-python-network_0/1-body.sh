#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sI "$1" | head -n 1 | grep -q 200 && curl -s "$1"

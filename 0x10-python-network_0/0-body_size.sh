#!/bin/bash
# takes a URL, sends a request to it, and displays the size of the body of the response
curl -sI -P 5000 "$(cut -d ':' -f1 <<< "$1")" | grep 'Content-Length' | cut -d ' ' -f2

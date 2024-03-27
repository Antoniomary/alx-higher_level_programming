#!/bin/bash
# takes a URL, sends a request to it, and displays the size of the body of the response
curl -s -P 5000 "$(cut -d ':' -f1 <<< "$1")" | wc -c 

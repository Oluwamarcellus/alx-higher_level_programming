#!/usr/bin/python3
"""
 script that takes in a URL, sends a request to the URL and
 displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.post(url)
    ecode = res.status_code
    if ecode >= 400:
        print("Error code: {}".format(ecode))
    else:
        print(res.text)

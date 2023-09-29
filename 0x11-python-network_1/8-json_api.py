#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    param = sys.argv[1] if sys.argv[1] else ""
    url = "http://0.0.0.0:5000/search_user"
    param = {"q": param}
    res = requests.post(url, data=param)
    res = res.json()
    if (type(res) is dict or type(res) is list):
        if res:
            id_ = res["id"]
            name = res["name"]
            print("[{}] {}".format(id_, name))
        else:
            print("No result")
    else:
        print("Not a valid JSON")

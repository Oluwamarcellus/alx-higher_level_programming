#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    param = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    param = {"q": param}
    res = requests.post(url, data=param)
    try:
        response = res.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")

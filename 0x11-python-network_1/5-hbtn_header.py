#!/usr/bin/python3
"""
python script that takes in a url and display the value of X-Request-Id
"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    req = requests.get(url)
    headers = req.headers
    print(headers.get('X-Request-Id'))

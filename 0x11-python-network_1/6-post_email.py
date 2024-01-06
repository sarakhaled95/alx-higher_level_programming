#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    r = requests.post(url, data=payload)
    print(r.text)

#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    payload = urllib.parse.urlencode(payload)
    payload = payload.encode('ascii')
    req = urllib.request.Request(url, payload)
    with urllib.request.urlopen(req) as response:
        data = response.read().data.decode('utf-8')
        print(data)

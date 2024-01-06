#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.error
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

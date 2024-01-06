#!/usr/bin/python3
"""
python script that takes in a url and display the value of X-Request-Id
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.getheaders()
        for header in headers:
            if header[0] == 'X-Request-Id':
                print(header[1])

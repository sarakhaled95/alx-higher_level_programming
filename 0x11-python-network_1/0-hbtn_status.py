#!/usr/bin/python3
"""
python script that fetches url
"""
if __name__ == "__main__":
    from urllib import request
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        data = response.read()
        print("body response:")
        print(f"    - type: {type(data)}")
        print(f"    - content: {data}")
        print(f"    - utf8 content: {data.decode('utf-8')}")

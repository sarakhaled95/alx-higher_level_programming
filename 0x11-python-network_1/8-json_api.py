#!/usr/bin/python3
"""
takes in a letter and sends a POST request
"""
if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    query = {'q': q}
    r = requests.post(url, data=query)
    if r.status_code != 200 or len(r.text) <= 0:
        print("No result")
        sys.exit()
    else:
        try:
            obj = r.json()
            if len(obj) == 0:
                print("No result")
                sys.exit()
            my_id = obj.get('id')
            my_name = obj.get('name')
            print(f"{[my_id]} {my_name}")
        except ValueError as invalid_jason:
            print("Not a valid JSON")

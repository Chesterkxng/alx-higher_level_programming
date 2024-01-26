#!/usr/bin/python3
"""
fetch data from https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode('utf-8'))

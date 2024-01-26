#!/usr/bin/python3
"""
 Response header value
"""
if __name__ == "__main__":
    import urllib.request
    import sys

    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        head = response.headers
        print(dict(head).get("X-Request-Id"))

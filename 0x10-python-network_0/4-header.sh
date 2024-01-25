#!/bin/bash
# takes in a URL as an argument, sends a GET request , and displays bdr
curl -s "$1" -H "X-School-User-Id: 98"

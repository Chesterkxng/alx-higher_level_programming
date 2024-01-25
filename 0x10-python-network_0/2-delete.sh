#!/bin/bash
# sends a DELETE request to the URL passed as the fst argument and displays bdr
curl -X DELETE -s "$1"

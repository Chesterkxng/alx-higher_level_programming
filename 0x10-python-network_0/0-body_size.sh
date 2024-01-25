#!/bin/bash
# Bash script that takes in a URL, send request then display size of body
curl -s -w "%{size_download}" -o /dev/null "$1" | { read size; echo "$size"; }

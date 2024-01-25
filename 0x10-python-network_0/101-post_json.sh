#!/bin/bash
# Sends a JSON POST request with given JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"

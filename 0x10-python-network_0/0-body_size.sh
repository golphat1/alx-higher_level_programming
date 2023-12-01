#!/bin/bash
# Bash script that takes in the URL, sends a request to that URL
curl -s "$1" | wc -c

#!/bin/bash
#script that takes in a URL and displays all HTTP methods the server will accept
curl -sI "$1" | awk '/Allow:/ { gsub(/^[ \t]+|[ \t]+$/, ""); print substr($0, index($0,$2)) }'

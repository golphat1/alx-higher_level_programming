#!/bin/bash
#request to 0.0.0.0:5000/catch_me causes server to respond
curl -sX PUT -d "user_id=you" "$1/catch_me" > /dev/null 2>&1

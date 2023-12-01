#!/bin/bash
#request to 0.0.0.0:5000/catch_me causes server to respond
grep -o 'You got me!' <<< "$(curl -s "$1")"

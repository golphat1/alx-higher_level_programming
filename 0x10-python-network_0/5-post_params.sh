#!/bin/bash
#script that takes url, sends post request, displays body
curl -s -X POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"

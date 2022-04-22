#!/bin/bash
#cURL a JSON file
curl -sX POST -H 'Content-Type: application/JSON' -d "@$2" "$1"

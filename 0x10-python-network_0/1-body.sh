#!/bin/bash
#cURL to the end
curl -s -i -L "$1" | tail -1

#!/bin/bash
#cURL only methods
curl -s -i -X OPTIONS "$1" | head -4 | tail -1 | cut -d " " -f2-

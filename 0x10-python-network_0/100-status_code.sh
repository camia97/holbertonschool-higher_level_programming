#!/bin/bash
#only status code
curl -s -o /dev/null -w "%{http_code}" 0.0.0.0:5000 ; echo ""

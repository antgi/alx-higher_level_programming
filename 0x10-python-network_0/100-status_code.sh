#!/bin/bash
# Will send a request to a URL passed as an argument and displays only the status code response
curl -s -o /dev/null -w "%{http_code}" "$1"

#!/bin/bash
# displays the status of code of the response
curl -L -s -X HEAD -w "%{http_code}" "$1"

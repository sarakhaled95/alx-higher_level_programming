#!/bin/bash
# script that was a fun effort in breaking to http protocols
curl -s -L -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me

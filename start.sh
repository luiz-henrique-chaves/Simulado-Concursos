#!/bin/bash

# Start nginx
service nginx start

# Start gunicorn
gunicorn --bind :8081 --workers 3 ryck.wsgi

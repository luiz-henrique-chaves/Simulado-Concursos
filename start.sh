#!/bin/bash

# Start nginx
service nginx start

# Start gunicorn
gunicorn --bind :8000 --workers 3 ryck.wsgi

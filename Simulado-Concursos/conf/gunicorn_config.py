command = '/usr/local/bin/gunicorn'
pythonpath = '/usr/local/bin/python3'
bind = "0.0.0.0:8000"
chdir = "/app/"
module = "ryck.wsgi:application"
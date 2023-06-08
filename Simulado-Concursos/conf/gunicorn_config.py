import multiprocessing

command = '/usr/local/bin/gunicorn'
pythonpath = '/usr/local/bin/python3'

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gthread'
threads = 4

chdir = "/app/"
module = "ryck.wsgi:application"

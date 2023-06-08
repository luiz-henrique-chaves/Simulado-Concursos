FROM python:3.10.8

WORKDIR /app

RUN apt-get update && apt-get install -y
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENV GUNICORN_CMD_ARGS="--worker-tmp-dir /dev/shm"
ENV WORKERS=2
ENV THREADS=4

CMD ["gunicorn", "--workers=$WORKERS", "--threads=$THREADS", "--worker-class=gthread", "-c", "conf/gunicorn_config.py", "ryck.wsgi"]

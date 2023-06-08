FROM python:3.10.8

WORKDIR /app

RUN apt-get update && apt-get install -y
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--config", "conf/gunicorn_config.py", "ryck.wsgi:application"]

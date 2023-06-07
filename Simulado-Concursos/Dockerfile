FROM python:3.10.8

WORKDIR /app

RUN apt update && apt upgrade -y && apt-get install -y nano
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 7000

CMD ["gunicorn", "-c", "conf/gunicorn_config.py", "ryck.wsgi"]
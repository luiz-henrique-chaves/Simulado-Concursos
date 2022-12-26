# Start from a python 3.11.0 alpine image
FROM python:3.11.0-alpine

RUN pip install --upgrade pip

# Copy the requirements file
COPY ./requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# copy all from Simulado-Concurso to app directory
COPY ./Simulado-Concursos /app

# Set the working directory
WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "entrypoint.sh" ]
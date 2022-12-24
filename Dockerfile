# Start from a Python 3.8 image
FROM python:3.8

# Set the working directory
WORKDIR /ryck

# Copy the requirements file
COPY requirements.txt /ryck/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the project
COPY . /app

# Collect static files
RUN python manage.py collectstatic --no-input

# Expose port 8000
EXPOSE 8000

# Start the server
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "ryck.wsgi"]

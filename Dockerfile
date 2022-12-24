# Start from a Python 3.8 image
FROM python:3.8

# Set the working directory
WORKDIR /ryck

# Copy the requirements file
COPY requirements.txt /ryck/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Install nginx
RUN apt-get update && apt-get install -y nginx

# Remove the default nginx configuration file
RUN rm /etc/nginx/sites-enabled/default

# Copy the nginx configuration file
COPY nginx.conf /etc/nginx/sites-enabled/

# Copy the rest of the project
COPY . /app

# Collect static files
RUN python manage.py collectstatic --no-input

# Expose ports 7000 and 8081
EXPOSE 7000
EXPOSE 8081

# Copy the start script
COPY start.sh /ryck/start.sh

# Make the start script executable
RUN chmod +x /ryck/start.sh

# Start the server
CMD ["/ryck/start.sh"]

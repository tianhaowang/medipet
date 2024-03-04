# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy specific file 
COPY ./app/endpoints.py ./endpoints.py

# Copy the requirements.txt file
COPY requirements.txt ./requirements.txt

# Copy database files
COPY ./database ./database

# copy aws files
COPY ./aws ./aws

# Install any needed packages specified in requirements.txt
RUN pip3 install --verbose --no-cache-dir -r requirements.txt

# Set Environment Variables for Database
ENV DB_HOST="mysql-container"
ENV DB_USER="root"
ENV DB_PASSWORD="password"
ENV DB_NAME="medibot"
ENV PYTHONPATH="/usr/local/lib/python3.10/site-packages:/app:/usr/bin:"
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV BUCKET_NAME='medibottian'

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run endpoints.py when the container launches
CMD ["python3", "./endpoints.py"]

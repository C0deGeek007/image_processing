# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /code/

# Install any additional dependencies for Celery if needed

# Example of how to start Celery (you may adjust this based on your project's structure)
CMD celery -A server worker --loglevel=info

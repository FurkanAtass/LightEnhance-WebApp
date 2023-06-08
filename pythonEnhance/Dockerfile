# Use the official Python base image with Python 3.7
FROM python:3.7-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy all files and directories from the local directory to the working directory in the container
COPY . /app

# Install the required packages
RUN pip install --default-timeout=300 -r requirements.txt

# Set the entrypoint command to run your Python app
CMD ["python", "enhanceApp.py"]

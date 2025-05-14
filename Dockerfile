# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 8080
EXPOSE 8080

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Command to run your app
CMD ["python", "app.py"]

# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the necessary dependencies
RUN pip install --no-cache-dir flask

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define the default command to run the app
CMD ["python3", "app.py"]

# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port the app runs on (adjust if necessary)
EXPOSE 5000

# Define the command to run the app (using python3 or flask, depending on the app)
CMD ["python3", "app.py"]

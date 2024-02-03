# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory within the container
WORKDIR /app

# Copy the Python script into the container
COPY fetch_data.py /app/

# Install required Python libraries
RUN pip install requests

# Run the script when the container starts
CMD ["python", "fetch_data.py"]
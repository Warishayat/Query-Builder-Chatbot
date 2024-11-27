# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /QueryBuilder-Chatbot

# Copy the current directory contents into the container at /QueryBuilder-Chatbot
COPY . /QueryBuilder-Chatbot

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8501


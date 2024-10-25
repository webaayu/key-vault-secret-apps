# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set environment variables
ENV LINK="http://www.cloudyuga.guru/"
ENV TEXT1="CloudYuga"
ENV TEXT2="Secret Rotation Example!"
ENV LOGO="https://raw.githubusercontent.com/cloudyuga/rsvpapp/master/static/cloudyuga.png"
ENV COMPANY="CloudYuga Technology Pvt. Ltd."

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir Flask

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

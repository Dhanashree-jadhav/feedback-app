# Use official Python image as base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy files from local machine to container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

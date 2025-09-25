# Use official Python image as base
FROM python:3.10-alpine

# Set working directory
WORKDIR /app

# Copy requirements if available
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port (change if your app uses a different port)
EXPOSE 5000

# Set default command (update if your entry point is different)
CMD ["python", "app.py"]
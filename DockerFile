FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files
COPY main.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "main.py"]

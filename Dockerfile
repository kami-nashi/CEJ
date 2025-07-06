FROM python:3.13-slim

WORKDIR /app

# Install tools you often use for debugging
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    iputils-ping \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Copy files and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set environment variable to avoid bytecode generation
ENV PYTHONUNBUFFERED=1

# Gunicorn command to launch the app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app.main:app"]
# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=school.settings

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port for the app
EXPOSE 8000

# Start the Django app using Gunicorn (recommended for production)
CMD ["gunicorn", "school.wsgi:application", "--bind", "0.0.0.0:8000"]

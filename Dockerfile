FROM python:3.10-slim

# Disable pyc files and buffer
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the full project
COPY . .

# ✅ Set ENV vars BEFORE collectstatic (required!)
ENV PYTHONPATH=/app
ENV DJANGO_SETTINGS_MODULE=school.settings

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run the app with Gunicorn
CMD ["gunicorn", "school.wsgi:application", "--bind", "0.0.0.0:8000"]

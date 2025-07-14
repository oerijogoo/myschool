FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set working directory
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

# Copy project files
COPY . .

# ✅ Set PYTHONPATH so Django can find 'school.settings'
ENV PYTHONPATH=/app

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start the app with Gunicorn
CMD ["gunicorn", "school.wsgi:application", "--bind", "0.0.0.0:8000"]

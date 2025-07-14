FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/myschool:/app \
    DJANGO_SETTINGS_MODULE=school.settings

# Create and set work directory
RUN mkdir -p /app/myschool
WORKDIR /app/myschool

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the entire project
COPY . .

# Verify the project structure
RUN ls -l && \
    ls -l school/

# Verify Python path resolution
RUN python -c "import sys; print('\n'.join(sys.path))"

# Verify settings can be imported
RUN python -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings'); from django.conf import settings; print(settings.BASE_DIR)"

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
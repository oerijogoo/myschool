FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
ENV DJANGO_SETTINGS_MODULE=school.settings

# Create and set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy ALL project files including the school directory
COPY . .

# Verify what was copied (debugging)
RUN ls -l && \
    echo "Contents of school directory:" && \
    ls -l school/ && \
    echo "Contents of school_app directory:" && \
    ls -l school_app/

# Run Django commands
RUN python manage.py collectstatic --noinput

EXPOSE 7903

CMD ["python", "manage.py", "runserver", "0.0.0.0:7903"]
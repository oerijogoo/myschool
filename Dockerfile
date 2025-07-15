FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
ENV DJANGO_SETTINGS_MODULE=school.settings

# Create and set working directory
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire project
COPY . .

# Verify the file structure
RUN ls -l

# Run collectstatic
RUN python manage.py collectstatic --noinput

EXPOSE 7903

CMD ["python", "manage.py", "runserver", "0.0.0.0:7903"]
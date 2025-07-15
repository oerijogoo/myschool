FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/myschool \
    DJANGO_SETTINGS_MODULE=school.settings

# Create and set working directory
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY ./requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire project
COPY . .

# Change to the project directory
WORKDIR /app/myschool

# Run collectstatic and migrations
RUN python manage.py collectstatic --noinput

EXPOSE 7903

CMD ["python", "manage.py", "runserver", "0.0.0.0:7903"]
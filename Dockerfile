FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=myschool.school.settings

# Create and set working directory
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY ./requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire project
COPY . .

# Verify the file structure (debugging line - can remove later)
RUN ls -l /app && ls -l /app/myschool

# Change to the correct directory where manage.py exists
WORKDIR /app/myschool

# Run collectstatic
RUN python manage.py collectstatic --noinput

EXPOSE 7903

CMD ["python", "manage.py", "runserver", "0.0.0.0:7903"]
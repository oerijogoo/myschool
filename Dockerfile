# Use official Python image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/myschool

# Set work directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY ./requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static files (adjust as needed)
RUN python myschool/manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "myschool/manage.py", "runserver", "0.0.0.0:8000"]
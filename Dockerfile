FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
ENV DJANGO_SETTINGS_MODULE=school.settings

# Create and set working directory
WORKDIR /app

# Install dependencies first (caching optimization)
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the ENTIRE project structure
COPY myschool/ .

# Verify the copied structure
RUN echo "Project structure:" && \
    find . -type d | sort && \
    echo "\nSchool directory contents:" && \
    ls -l school/ && \
    echo "\nSchool_app directory contents:" && \
    ls -l school_app/

# Run Django commands
RUN python manage.py collectstatic --noinput

EXPOSE 7903
CMD ["python", "manage.py", "runserver", "0.0.0.0:7903"]
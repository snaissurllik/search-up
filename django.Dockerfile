# Use an official Python runtime as a parent image
FROM python:3.10-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app


# Set environment variables
ENV PYTHONUNBUFFERED 1

# Expose port 8000 for the Django application
EXPOSE 8000

# Run sleep.py script, migrations and start the server
CMD ["sh", "-c", "python sleep.py && \
    python manage.py makemigrations; \
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000"]


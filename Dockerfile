# Dockerfile

# Use official Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE: oc_lettings_site.settings
ENV ALLOWED_HOSTS=python-oc-lettings-latest.onrender.com
ENV DEBUG=False
ENV DB_URL=oc-lettings-site.sqlite3

# Create working directory
WORKDIR /OC-lettings

# Copy requirements and install dependencies
COPY requirements.txt /OC-lettings/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /OC-lettings/

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

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
ENV SENTRY_DSN=https://0bb44f8058ea87888f4f0076f3f7c918@o4508400685088768.ingest.de.sentry.io/4508400688037968

# Create working directory
WORKDIR /OC-lettings

# Copy requirements and install dependencies
COPY requirements.txt /OC-lettings/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files to the directory
COPY . /OC-lettings/

# Collect static files
# https://docs.djangoproject.com/en/5.1/ref/contrib/staticfiles/
RUN python manage.py collectstatic --noinput --clear

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]

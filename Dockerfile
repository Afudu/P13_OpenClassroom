# Dockerfile

# Use official Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings
ENV SECRET_KEY='fp$9^593hsriajg$+%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s'
ENV ALLOWED_HOSTS=python-oc-lettings-latest.onrender.com
ENV DEBUG=False
ENV DB_NAME=oc-lettings-site.sqlite3
ENV SENTRY_DSN='https://0bb44f8058ea87888f4f0076f3f7c918@o4508400685088768.ingest.de.sentry.io/4508400688037968'

# Create working directory
WORKDIR /OC-lettings

# Copy requirements and install dependencies
COPY requirements.txt /OC-lettings/
RUN pip install --upgrade pip && pip install -r requirements.txt


# Copy project files to the repository
COPY . /OC-lettings/

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

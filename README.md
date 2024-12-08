# OpenClassrooms - Python Developer Path

**Project 13:** Scale a Django Application Using Modular Architecture

**Student:** Abdoul Baki Seydou

**Date:** 10/09/2024

## Summary

The project consists of improving the 
[initial website](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings) 
of Orange County Lettings, a startup in the property rentals industry, 
both in terms of the code and its deployment.

The website is built with Django, a Python framework, and uses an SQLite database.

The improvements to add the website are broken into four steps:
   1. Miscellaneous technical debt refactor.
   2. Modular architecture refactor.
   3. CI/CD pipeline and deployment.
   4. Production error logging using Sentry.

## Local development

### Prerequisites

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher

In the rest of the local development documentation, it is assumed the command `python` in 
your OS shell runs the above Python interpreter (unless a virtual environment is activated).

### macOS / Linux

#### Clone the repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings.git`

#### Create the virtual environment

- `cd /path/to/Python-OC-Lettings`
- `python -m venv venv`
- `apt-get install python3-venv` (If previous step errors with package not found on Ubuntu)
- Activate the environment `source venv/bin/activate`
- Confirm the command `python` now runs the Python interpreter in the virtual environment,
`which python`
- Confirm the version of the Python interpreter is 3.6 or higher `python --version`
- Confirm the command `pip` runs the pip executable in the virtual environment, `which pip`
- To deactivate the environment, `deactivate`

#### Run the site

- `cd /path/to/Python-OC-Lettings`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Go to `http://localhost:8000` in a browser.
- Confirm the site is running and can be navigated (you should see several profiles and lettings).

#### Linting

- `cd /path/to/Python-OC-Lettings`
- `source venv/bin/activate`
- `flake8`

#### Unit tests

- `cd /path/to/Python-OC-Lettings`
- `source venv/bin/activate`
- `pytest`

#### Database

- `cd /path/to/Python-OC-Lettings`
- Open a shell session `sqlite3`
- Connect to the database `.open oc-lettings-site.sqlite3`
- Display tables in the database `.tables`
- Display columns in the profiles table, `pragma table_info(Python-OC-Lettings_profile);`
- Run a query on the profiles table, `select user_id, favorite_city from
  Python-OC-Lettings_profile where favorite_city like 'B%';`
- `.quit` to exit

#### Admin panel

- Go to `http://localhost:8000/admin`
- Login with user `admin`, password `Abc1234!`

### Windows

Using PowerShell, as above except:

- To activate the virtual environment, `.\venv\Scripts\Activate.ps1` 
- Replace `which <my-command>` with `(Get-Command <my-command>).Path`

## Deployment

### Prerequisites
- GitHub repository for the application.
- [Docker Hub](https://hub.docker.com/) account.
- [Render](https://render.com/) account with a web app service set up for an existing image.
- [Sentry](https://sentry.io/signup/) account for a Django project.

### Overview
The website is deployed using a CI/CD pipeline using GitHub Actions.

The deployment workflow involves:
- The code is linted and tested before deployment.
- A Docker image is built, tagged, and pushed to Docker Hub.
- The image is deployed to Render, a cloud hosting service.

* Note: Store account credentials as GiHub secrets.

### Configuration
The configuration involves:
1. Production error logging using Sentry:
   - Set up the Sentry account created in the Django application settings.
   - Sentry automatically assigns a Data Source Name (DSN).
2. Docker Hub repository:
   - Create a repository to store images created during containerization.
3. A Dockerfile.
   - Create a Dockerfile in the root of the project repository.
4. Render setup:
   - Create a new web app service for an existing image.
   - Get the Render deploy hook URL from the web app settings.
   - Get the deployed app URL from the web app settings.
5. Account credentials set up as GitHub secrets.
6. GitHub actions Workflow creation placed in ```.github/workflows``` located in the root.

* Note: Store secrets as environment variables.

### Steps
To run the deployment:

1. Push changes to the master branch.
2. The pipeline runs automatically, performing the following jobs:
   - Build-and-Test
   - Containerization
   - Deploy to Production.

* Note: 
  - Changes to the master branch trigger all three jobs.
  - Changes to other branches only trigger the build-and-test job.

The deployment can be created anytime by rerunning the pipeline.

The OC Lettings's website is deployed to Render with all required improvements, and is available at: 

https://python-oc-lettings-latest.onrender.com/
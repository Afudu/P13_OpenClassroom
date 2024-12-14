# Scale a Django Application Using Modular Architecture

**Project 13**  

**Student:** Abdoul Baki Seydou

**Date:** 10/09/2024  

## Table of Contents
1. [Summary](#summary)
2. [Technologies Used](#technologies-used)
3. [Immediate Tasks](#immediate-tasks)
4. [Local Development](#local-development)
   - [Prerequisites](#prerequisites)
   - [Setup on macOS/Linux](#setup-on-macoslinux)
   - [Setup on Windows](#setup-on-windows)
   - [Running the Application](#running-the-application)
   - [Linting and Testing](#linting-and-testing)
   - [Database Management](#database-management)
   - [Admin Panel](#admin-panel)
5. [Deployment](#deployment)
   - [Prerequisites](#deployment-prerequisites)
   - [Overview](#overview)
   - [Configuration](#configuration)
   - [Steps to Deploy](#steps-to-deploy)
   - [Live Application](#live-application)

----

## Summary
This project involves improving the [OC Lettings website](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings), 
focusing on code quality and deployment enhancements.
The improvements include modular architecture, CI/CD implementation, and production error logging.

----

## Technologies Used
- **Programming Language:** Python  
- **Framework:** Django  
- **Database:** SQLite  

---

## Immediate Tasks
The improvements are divided into the following parts:
1. Refactoring to address technical debt.
2. Transitioning to a modular architecture.
3. Implementing CI/CD pipeline and automated deployment.
4. Integrating Sentry for production error logging.

---

## Local Development

### Prerequisites
- GitHub account with repository access.
- Git CLI.
- SQLite3 CLI.
- Python 3.6 or higher.

---

### Setup on macOS/Linux

1. **Clone the Repository**
   ```bash
   cd /path/to/put/project/in
   git clone https://github.com/Afudu/P13_OpenClassroom.git

2. **Move to the folder**
   ```bash
   cd P13_OpenClassroom

3. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   
4. **Activate Environment**
   ```bash
   source venv/bin/activate 

5. **Securely upgrade pip**
   ```bash
   python -m pip install --upgrade pip 

6. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
7. **To deactivate Environment**
   ```bash
   deactivate

---

### Setup on Windows

1. Follow the steps above.

2. To activate the environment:
   ```bash
   .\venv\Scripts\Activate
   
---

### Running the application

1. **Start the server**
   ```bash
   python manage.py runserver
   
2. **Access in the browser**
   To verify the site is running, navigate to:
   ```bash
   http://localhost:8000

---

### Linting and Testing

- **Run Linting**
  ```bash
  flake8

- **Run Unit Tests**
  ```bash
  pytest 

---

### Database Management

- **Open SQLite shell:**
  ```bash
  sqlite3
  
- **Connect to the database:**
  ```sql
  .open oc-lettings-site.sqlite3
  
- **View tables:**
  ```sql
  .tables
  
- **Query profiles table:**
  ```sql
  select user_id, favorite_city from Python-OC-Lettings_profile where favorite_city like 'B%';
  
- **Exit shell:**
  ```sql
  sqlite3

---

### Admin Panel
1. Navigate to http://localhost:8000/admin
2. Use login credentials:
   - Username: admin
   - Password: Abc1234!

---

## Deployment

### Deployment Prerequisites
- GitHub repository.
- Docker Hub account.
- Render account with a web app service.
- Sentry account for Django.

---

### Overview
Deployment uses a CI/CD pipeline with GitHub Actions, involving:
1. Linting and testing code.
2. Building and pushing Docker images.
3. Deploying to Render.

---

### Configuration
1. **Sentry:** Configure DSN in Django settings.
2. **Docker Hub:** Create a repository for container images.
3. **Dockerfile:** Add at the root of the project.
4. **Render:** Set up a web app service for the container image.
5. **GitHub Secrets:** Store account credentials securely.
6. **Workflow:** Place configuration in .github/workflows.

---

### Steps to Deploy
1. Push changes to the master branch.
2. The pipeline will:
   - Build and test the code.
   - Build and push Docker images.
   - Deploy to production.

   **Note:** Changes to non-master branches only trigger the build-and-test step.

---

### Live Application

- The website is live at:

   https://python-oc-lettings-latest.onrender.com/
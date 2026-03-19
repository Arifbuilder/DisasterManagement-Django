---
description: Set up the environment and run the Disaster Management project.
---

This workflow automates the first-time setup for the Disaster Management project, including virtual environment creation, dependencies installation, and starting the local development server.

// turbo-all
1. Use the `run_command` tool to create a Python virtual environment:
   `python -m venv venv`
2. Use the `run_command` tool to activate the environment and install dependencies:
   `venv\Scripts\pip install -r requirements.txt`
3. Use the `run_command` tool to create and apply database migrations:
   `venv\Scripts\python manage.py makemigrations`
4. Use the `run_command` tool to apply those migrations:
   `venv\Scripts\python manage.py migrate`
5. Use the `run_command` tool to run the development server:
   `venv\Scripts\python manage.py runserver`

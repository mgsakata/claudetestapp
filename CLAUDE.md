# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

All commands assume the virtual environment is active (`source .venv/bin/activate`).

```bash
# Run development server
python manage.py runserver

# Apply migrations
python manage.py migrate

# Create a new migration after model changes
python manage.py makemigrations

# Run all tests
python manage.py test

# Run tests for a specific app
python manage.py test <app_name>

# Run a single test
python manage.py test <app_name>.tests.TestClassName.test_method_name

# Open Django shell
python manage.py shell

# Create a new Django app
python manage.py startapp <app_name>
```

## Architecture

This is a Django 6.0.7 project using a **config-as-package** layout: the Django project package is named `config/` (rather than the app name), containing `settings.py`, `urls.py`, `wsgi.py`, and `asgi.py`. The root `manage.py` points to `config.settings`.

**Environment configuration** is handled by `python-decouple`, which reads from `.env` in the project root. Required variables: `SECRET_KEY`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`.

**Database**: PostgreSQL (configured in `config/settings.py` via decouple). There is no SQLite fallback.

New Django apps should be created in the project root and registered in `INSTALLED_APPS` in [config/settings.py](config/settings.py). URL patterns for new apps are added to [config/urls.py](config/urls.py) using `include()`.

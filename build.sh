#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Install all Python dependencies
pip install -r requirements.txt

# 2. Run Django's collectstatic to gather all static files into STATIC_ROOT
python manage.py collectstatic --no-input

# 3. Apply any database migrations
python manage.py migrate
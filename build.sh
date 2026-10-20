
#!/usr/bin/env bash
# Exit on error
set -o errexit

# 1. Install all Python dependencies
pip install -r requirements.txt

# 2. Apply database migrations
python manage.py migrate --no-input

# 3. Collect static files
python manage.py collectstatic --no-input

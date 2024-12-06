#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this  line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt



# Create database tables in order
echo "Making migrations..."
python manage.py makemigrations

echo "Migrating auth..."
python manage.py migrate auth

echo "Migrating admin..."
python manage.py migrate admin

echo "Migrating contenttypes..."
python manage.py migrate contenttypes

echo "Migrating sessions..."
python manage.py migrate sessions

echo "Migrating remaining apps..."
python manage.py migrate

# Convert static asset files
python manage.py collectstatic --no-input

# Create superuser if needed (can be commented out after first run)
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell
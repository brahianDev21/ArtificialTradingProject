#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this  line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt



# Reset migrations and database
echo "Resetting database..."
python manage.py migrate --fake zero

# Create database tables in strict order
echo "Creating database tables..."
python manage.py migrate contenttypes --noinput
python manage.py migrate auth --noinput
python manage.py migrate admin --noinput
python manage.py migrate sessions --noinput

echo "Migrating remaining apps..."
python manage.py migrate --noinput

# Convert static asset files
python manage.py collectstatic --no-input

# Create superuser
echo "Creating superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

echo "Build completed."
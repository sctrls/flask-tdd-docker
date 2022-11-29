#!/bin/sh

echo "Waiting for postgres..."

# netcat scan for listening daemons at 5432 in api-db
while ! nc -z api-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py run -h 0.0.0.0
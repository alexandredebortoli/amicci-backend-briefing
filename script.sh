#!/bin/bash
echo "CREATE MIGRATIONS"
python manage.py makemigrations briefing_api
echo "=========================="

echo "MIGRATE"
python manage.py migrate
echo "=========================="

echo "TESTS"
python manage.py test
echo "=========================="

echo "START SERVER"
python manage.py runserver 0.0.0.0:8000

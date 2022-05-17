#!/bin/sh

python3 manage.py migrate
python3 manage.py create_superuser
python3 manage.py add_product
sleep 5
python3 manage.py runserver 0.0.0.0:8080

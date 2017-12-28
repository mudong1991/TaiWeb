#!/bin/bash
echo '---------------migrate database main------------------------'
docker exec -it taileizi python manage.py migrate

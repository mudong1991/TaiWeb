#!/bin/bash
echo "Packaging taileizi project ......"
tar -cf taileizi.tar -C ../ ./
echo "Build mudong/taileizi docker image start ......"
docker build -t mudong/taileizi ./
echo "Start container taileizi ......"
docker run --name taileizi -v /var/www/taileizi -p 8810:8000 -d mudong/taileizi /usr/local/bin/uwsgi --http :8000 --chdir /var/www/taileizi --static-map /static=/var/www/taileizi/static --static-map /media=/var/www/taileizi/media -w TaiWeb.wsgi

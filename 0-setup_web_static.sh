#!/usr/bin/env bash
# Setup ur own nginx config

# update and check inginx file
apt-get update
apt-get install nginx -y

# Make folders
mkdir -p /data/web_static/shared/test
mkdir -p /data/web_static/shared/
echo "Welcome Everybody" >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/currect
chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
# RESTART NGNIX
service nginx start

#!/usr/bin/env bash
# install Nginx make folders
apt-get update
apt-get install nginx -y
sudo mkdir -p /data /data/web_static/

sudo mkdir -p /data/web_static/releases/test/ 
sudo mkdir -p /data/web_static/shared/
echo "Welcome Everybody" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
# restart nginx
sudo service nginx restart

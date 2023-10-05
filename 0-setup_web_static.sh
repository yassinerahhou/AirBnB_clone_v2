#!/usr/bin/env bash
# install Nginx if not already installed and creat new folder
sudo su
apt-get update
apt-get install nginx -y
mkdir -p /data /data/web_static/

mkdir -p /data/web_static/releases/test/ 
mkdir -p /data/web_static/shared/
echo "test hh test hh test hh" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
service nginx restart

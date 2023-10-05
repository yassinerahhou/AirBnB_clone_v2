#!/usr/bin/env bash
<<<<<<< HEAD
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
=======
# sets up the web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
>>>>>>> a671dcd3b702e54e393b2bfc78c4e71a932813d2

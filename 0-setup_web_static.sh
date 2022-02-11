#!/usr/bin/env bash
# Config Server
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install -y nginx
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared
echo "<h1>Holberton School</h1>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown ubuntu:ubuntu -hR /data/
sudo sed -i '40i \\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart

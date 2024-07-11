#!/usr/bin/env bash
# Bash scrit that setup a web server for deployment

if ! dpkg -l | grep -q nginx; then
    sudo apt update
    sudo apt install -y nginx
fi

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo "<html>
  <head>
  </head>
  <body>
    Welcome to web_static!
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

nginx_config="/etc/nginx/sites-available/default"
sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' $nginx_config

sudo systemctl restart nginx

exit 0

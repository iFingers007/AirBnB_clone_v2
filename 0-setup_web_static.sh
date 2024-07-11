#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

sudo apt-get update -y

if ! command -v nginx &> /dev/null
then
    sudo apt-get install nginx -y
fi

sudo mkdir -p /data/ /data/web_static/ /data/web_static/releases/  /data/web_static/shared/ /data/web_static/releases/test/

echo "\
<html>
  <head>
  </head>
  <body>
    iFingers Tech
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

TD="/data/web_static/releases/test/"
SN="/data/web_static/current"

if [ -L "$SN" ]; then
    rm "$SN"
fi

sudo ln -s "$TD" "$SN"

sudo chown -R ubuntu:ubuntu /data/

CFG_FILE="/etc/nginx/sites-enabled/default"

if ! grep -q "location /hbnb_static" $CFG_FILE; then
    sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}' $CFG_FILE
fi

sudo service nginx restart

#!/bin/bash
sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-available/default
echo files deleted
sudo /etc/init.d/nginx stop
sudo ln -s /home/box/web/etc/ngix.conf /etc/nginx/sites-enabled/default
echo  "Configuration done"
sudo /etc/init.d/nginx start

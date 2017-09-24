#!/bin/bash
sudo /etc/init.d/nginx stop
sudo ln -s /home/box/web/etc/ngix.conf /etc/nginx/sites-enabled/default
echo  "Configuration done"
sudo /etc/init.d/nginx start

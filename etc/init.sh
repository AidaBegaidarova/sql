#!/bin/bash
sudo rm -f /etc/nginx/sites-enabled/default
sudo rm -f /etc/nginx/sites-available/default

sudo ln -sf /home/box/web/etc/ngix.conf /etc/nginx/site-enabled/default
sudo /etc/init.d/nginx restart

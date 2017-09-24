#!/bin/bash
sudo rm -f /etc/nginx/sites-enabled/default
sudo rm -f /etc/nginx/sites-available/default
echo files deleted
sudo ln -s /home/box/web/etc/ngix.conf /etc/nginx/sites-enabled/text.conf
echo  "Configuration done"
sudo /etc/init.d/nginx restart

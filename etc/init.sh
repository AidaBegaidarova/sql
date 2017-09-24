sudo unlink /etc/nginx/sitex-enabled/default
sudo ln -s /home/box/web/etc/ngix.conf /etc/nginx/sites-enabled/default
echo  "Configuration done"
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
echo "Unicorn done"
sudo /etc/init.d/gunicorn restart


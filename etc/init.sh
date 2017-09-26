sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
echo  Configuration done
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test_wsgi
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test_django
echo Unicorn done
sudo /etc/init.d/gunicorn restart
echo setting up mysql
sudo /etc/init.d/mysql start
sudo mysql -u root -e "create database ask"
# Profiles rest api

vagrant init ubuntu/bionic64
vagrant up
vagrant ssh
cd /vagrant/
source ~/env/bin/active
pip install -r requirements.txt
django-admin startproject profiles_project .
python manage.py startapp profiles_api
python manage.py runserver 0.0.0.0:8000
127.0.0.1:8000


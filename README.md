# django-base
The purpose of this repository is to provide the basic outline for creating a base for a Django app which can then be containerized. You can run Django using `venv` or containerizing it in Docker.

## Update System
```bash
sudo apt update
sudo apt upgrade
```

## Install Python VENV package
```bash
sudo apt install python3.12-venv
```

Create Virtual Environment
```bash
python3 -m venv projectname
```

Activate virtual environment
```bash
source /bin/activate
```

# Install Dependencies (Django is in the requirements.txt file)
```bash
pip install -r requirements.txt 
```

Check Version
```bash
django-admin --version
```

Create a Project (no hyphens)
```bash
django-admin startproject projectname
```

This will create some sort of output like the following
```bash
projectname  
   manage.py  
   projectname/  
       __init__.py  
       asgi.py  
       settings.py  
       urls.py  
       wsgi.py
```

Go into the new project directory
```bash
cd projectname
```

Run the Development Server Locally to see if this works (use a port you're not currently using)
```bash
python manage.py runserver 0.0.0.0:8000
```

If not running locally, update settings.py with allowed_hosts = [*] or add the IP of the server

Create a Django App
```bash
python manage.py startapp appname
```

This will be the project structure now
```bash
projectname  
   manage.py
   projectname/  
   appname/
       migrations/  
           __init__.py  
       __init__.py  
       admin.py  
       apps.py  
       models.py  
       tests.py  
       views.py
```
Create auth tables and super user
```bash
python manage.py migrate
python manage.py createsuperuser
```

Modify your `settings.py` file and add the name of your app (e.g. appname) and the `requests` and `rest_framework library`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'appname',
    'requests',
    'rest_framework'
]
```

Save and run the following:
```bash
python manage.py runserver 0.0.0.0:8000
```

Navigate to the hostname/ip address on port 8000. Navigate to <host-ip>:8000/admin and test a log in with the super user you just created.

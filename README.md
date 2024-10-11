# django-base
The purpose of this repository is to provide the basic outline and necessary dependencies for creating a **Django API application** which can then be containerized in another step/tutorial (coming soon!!). This should at least get you started!! 

## Prerequisites
- Python3

# Building Manually
If you would like to build this all manually, follow the steps below.

## Update System (Linux)
```bash
sudo apt update
sudo apt upgrade
```

## Install Python `venv` package (Linux)
```bash
sudo apt install python3-venv
```

## Install Python `venv` package (Windows)
```powershell
pip install virtualenv
```

Create Virtual Environment with a `venv_projectname` of your choice:
```bash
python3 -m venv venv_projectname
```

Change into the new directory:
```bash
cd venv_projectname
```

Activate virtual environment:
```bash
source bin/activate
```

# Install Dependencies
## Contents of the `requirements.txt`:
```sh
Django==5.1.1
django-filter==24.3
djangorestframework==3.15.2
Markdown==3.7
requests==2.32.3
```

# Project Dependencies

This project uses the following Python packages:

## Django==5.1.1
This is the actual Django package. Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Version 5.1.1 includes new features like the `querystring` template tag for easier URL parameter handling, PostgreSQL connection pools, and the `LoginRequiredMiddleware` for default authentication.

## django-filter==24.3
This package is used if you're needing to build out filters without using some crazy Python code. The package provides a reusable Django application for adding dynamic QuerySet filtering from URL parameters. It allows users to filter querysets based on user selections, making it easier to build complex search functionalities.

## djangorestframework==3.15.2
The Django REST framework is what will make the Django app super powerful in that it provides you with the framework for the API backend. It's a powerful and flexible toolkit for actually building Web APIs. It includes features like:
- A Web browsable API
- Authentication policies
- Serialization that supports both ORM and non-ORM data sources

## Markdown==3.7
This is a Python implementation of John Gruber's Markdown, a lightweight markup language for creating formatted text using a plain-text editor. It supports various extensions and is almost completely compliant with the reference implementation.

## requests==2.32.3
Requests is an elegant and simple HTTP library for Python, designed for human beings. It allows you to send HTTP/1.1 requests easily, with features like keep-alive, connection pooling, and automatic content decoding. Something like the following can be done to easily pull data:

```python
import requests
url = "https://github.com"
response = requests.get(url)
if response.status_code == 200:
    print(response.text)
```

Go ahead and install the above requirements.
```bash
pip install -r requirements.txt 
```

Check Django Version installed:
```bash
django-admin --version
```

Create a Project (no hyphens). `django_projectname` is the name of your project.
```bash
django-admin startproject django_projectname
```

This will create some sort of output like the following. You can view tree structures by running the `tree` command in your terminal.
```bash
.
├── db.sqlite3
├── django_projectname
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

Go into the new project directory
```bash
cd django_projectname
```

Run the Development Server Locally to see if this works (use a port you're not currently using. I'm using port 8000 for my purposes)
```bash
python manage.py runserver 0:8000
```
Navigate to `https://localhost:8000`:
![image](https://github.com/user-attachments/assets/e3dcc00b-8216-4422-add0-ce8e48444c93)


Next, you'll need to create your first app. Replace `django_appname` with the name of your app.
```bash
python manage.py startapp django_appname
```

This will be the project structure now. 
```bash
.
├── db.sqlite3
├── django_appname
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── django_projectname
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── settings.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   └── wsgi.cpython-312.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```
Now that you have your project and first app creation out of the way, you'll want to authenticate and log into the built-in `/admin` panel Django provides. For this, we'll need to populate the `sqlite` database that was automatically created with the appropriate tables that are used on the backend to handle authentication. You'll run the `migrate` feature first and then you'll create a superuser using the `createsuperuser` command.
```bash
python manage.py migrate
```

This will create an output like this:
```bash
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

Create your user:
```bash
python manage.py createsuperuser
```
Output:
```bash
user@host:~/django_project/django_base$
  Username (leave blank to use '<your username>'): 
  Email address: 
  Password: 
  Password (again): 
  Superuser created successfully.
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

    'django_appname',
    'requests',
    'rest_framework'
]
```

Save and run the following:
```bash
python manage.py runserver 0:8000
```

Navigate to `https://localhost:8000/admin` to log into Django with the username and password you created when you set up your superuser.

![image](https://github.com/user-attachments/assets/adb8e280-09a3-4120-830a-e2207c666000)

Once logged in, this is the dashboard you'll be able to view registered tables, create users, create groups, change passwords, and various other features you can navigate here: [Django Admin](https://docs.djangoproject.com/en/5.1/ref/contrib/admin/)
![image](https://github.com/user-attachments/assets/452694d6-1137-44c5-bdab-139a08969fa5)

Now that you have the app name registered, the `requests` and `rest_framework` packages integrated, you can start building an API (instructions coming soon)

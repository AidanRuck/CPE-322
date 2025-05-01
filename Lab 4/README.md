# Lab 4 - Django and Flask
### *"I pledge my honor that I have abided by the Stevens Honor System." -Aidan Ruck*

## Introduction to the Lab
This lab is an introduction to Django and Flask. Django is a framework which allows for rapid development, while Flask is more aimed for building web applications. This lab is to show how to setup and run projects with Django, and later run servers using Flask.

## Required Dependencies
The following dependencies are needed to run the projects discussed in this lab. Please run the following commands:
```
pip install setuptools
pip install django
pip install djangorestframework
pip install django-filter
pip install markdown
pip install requests
pip install flask
```
## Starting Django Project
![image](https://github.com/user-attachments/assets/fb80332d-5083-4e65-9f63-c8c846bcde45)
As seen in the image, I started by creating a new project named 'stevens.'

## Starting Django App
![image](https://github.com/user-attachments/assets/fda3ea7a-c499-47b2-bed3-07e65c6830b8)
Then, I created an App named 'myapp' within the stevens directory.

## Setting up SQLite Database
![image](https://github.com/user-attachments/assets/000f6259-0f1d-42d9-94e9-7ac2164c0777)
Because I run a Windows Machine, I had to swtich over to Git Bash to simulate the Linux environment. I then created a new SQLite Database using `python manage.py migrate`.

## Editing settings.py
![image](https://github.com/user-attachments/assets/6825d360-034c-4918-bc83-36ad8ca60e44)
![image](https://github.com/user-attachments/assets/ed49a71e-0609-4add-8067-01194d60d1f1)
To properly set the project up, many of the initial settings need to be changed. In order to do so, I used `nano settings.py.` First, I added an asterisk (signalling all) to ALLOWED_HOSTS. Then, the INSTALLED_APPS list should have myapp added. Finally, I changed the timezone to America/New_York to show the correct time.


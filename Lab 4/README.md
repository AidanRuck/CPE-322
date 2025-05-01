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

## Copying urls.py, admin.py, models.py, and views.py
![image](https://github.com/user-attachments/assets/9fb0caa0-9214-45f7-97e9-201fc265259d)  
I then added urls.py to the stevens directory, then the other 3 files to the myapp directory with the commands above.

## Copying index.html
![image](https://github.com/user-attachments/assets/79468dc3-2db0-4eb2-9198-b87a80503fe2)  
Similar to above, I created new directories and copied the index.html files over.

## Configure Google Maps API
I had to create an account on Google Maps Platform to generate an API key. After logging in, and providing credentials, I then used `nano index.html` to write the API key into the text. I have not provided a picture as to secure my private details.

## Copying the Static files
![image](https://github.com/user-attachments/assets/773d8b42-a963-4fa3-af95-6301acbc8b69)  
To diplay the website properly, I had to copy these files into the places specified in the commands.

## Creating a Django Admin Account
![image](https://github.com/user-attachments/assets/9da169d7-da62-4751-96da-7fa8408534e1)  
![image](https://github.com/user-attachments/assets/633d6f8d-04f2-4bab-9ef0-8a48110e21df)  
To have an Admin account on the server, I had to make a superuser account. The line `python manage.py createsuperuser` did not work, but following a suggestion from another class member, `winpty python manage.py createsuperuser` did work.

## Running the Django Server
![image](https://github.com/user-attachments/assets/0dfc79da-844a-40f1-a283-b627a9f60b45)  
Since everything has now been configued, I ran the server using the command `python manage.py runserver`. After that, I was able to open the App by navigating to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin). After that, I input the current temperature data with the date, time, and location.

## Viewing from Client Side
To see from the client side, you can navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the data that you have input.

## Creating a (NEW) Django REST Project
![image](https://github.com/user-attachments/assets/d9fca2c4-bd9e-4cee-a3c7-4deed3246d7b)  
Just as before, I created a new Django project called mycpu.

## Starting the new Django App
![image](https://github.com/user-attachments/assets/230a6661-52cd-4935-a48b-d2f2a733bbc4)  
Using the commands, I created a new app called myapp.

## Editing settings.py
![image](https://github.com/user-attachments/assets/08e639a0-9296-438b-92b9-f68989ad94cb)  
![image](https://github.com/user-attachments/assets/4df47f48-2fe4-42dd-abdb-7805bfacb656)  
Like above, I used `nano settings.py` to change the necessary settings. I changed ALLOWED_HOSTS to an asterisk (to denote any), added myapp and rest_framework to INSTALLED_APPS, and then changed the timezone to New York.

## Copying ursl.py, admin.py, views.py, models.py, and serializers.py
![image](https://github.com/user-attachments/assets/fdfdab74-9ca5-48d0-bd91-72c584b0d1ff)  
Like above, I copies urls.py into the mycpu directory, then added admin.py, views.py, models.py, and serializers.py to myapp's directory.

## Copying index.html
![image](https://github.com/user-attachments/assets/3d2de533-cc35-4032-a668-83fcde3ef8dd)  
I created new directories and copied index.html into one as shown above.

## Edit index.html
I used the same API Key I had generated from above to copy into index.html using `nano index.html`.

## Copy Static Files
![image](https://github.com/user-attachments/assets/bb28a6cc-1215-4437-bdcd-418dc2542b34)  
As before, I copied all of the CSS and JavaScript files into this project (static files).

## Copy controller.py to ~/mycpu
![image](https://github.com/user-attachments/assets/d1c1a9ae-0de1-46d3-b7c1-c1f63c57379e)  
As this project uses the REST framework, it needs extra files. One of these is controller.py. The program controller.py sends data to the server, allowing it to be displayed within the website.

## Creating Admin account
![image](https://github.com/user-attachments/assets/c1c8748c-539f-4a01-a51d-2185c1a9fe86)  
Using the same lines as above, I finished setting the sever and created an admin account.

## Run Server
![image](https://github.com/user-attachments/assets/1ce9d514-21bd-49d4-bafd-3222ab1f436c)  
To run the server, I again used `python manage.py runserver`. I then connected to it at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). After adding the Latitude and Longitude of Stevens Institute of Technology, I then went to each link. At [http://127.0.0.1:8000/dt/](http://127.0.0.1:8000/dt/) I added 2025, at [http://127.0.0.1:8000/cpu/](http://127.0.0.1:8000/cpu/) I added 20, and at [http://127.0.0.1:8000/mem](http://127.0.0.1:8000/mem) I added 20 as well.  
![image](https://github.com/user-attachments/assets/3e7cbf6d-a4ea-45c5-b1a0-3722a8cc8da6)  
Then, I opened another terminal window to run the controller.py program.

## Client View
You can then view the site at [127.0.0.1:8000/home](127.0.0.1:8000/home). At this site, you will see the location that you entered via Google Maps, as well as your CPU information from controller.py.

## Running a Flask Server
![image](https://github.com/user-attachments/assets/e49afb1e-d244-476e-a064-86a411ac6d1d)  
To run this server, I navigated into the lesson4 directory to run the hello_world.py file. After running the command, I went to [http://127.0.0.1:500/](http://127.0.0.1:500/) to view it.  
![image](https://github.com/user-attachments/assets/b25707d6-23c2-4c7f-bc40-98065a42aaf9)

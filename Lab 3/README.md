# Lab 3 - Python
### *"I pledge my honor that I have abided by the Stevens Honor System" - Aidan Ruck*

## Introduction to the Lab
This lab is meant to introduce students to Python and the different packages that one can install. These packages are used to outsource conversions or programs that may be needed within your own work.

## Required Packages
* jdcal
** This is a package for converting from the Gregorian Calendar (what the United States and most countries use) to the Julian Calendar
* astral
** The 'astral' package is for calculations with different astrological-based properties. Some of them include sunrise and sunset times, solar elevation, moon phase, etc..
* geopy
** This provides multiple APIs for geolocation services (such as Google Maps)
* pytz
** This allows for conversions between timezones
* psutil
** This package provides information which regards processes, system utilization, and statistics.

## Lab Setup
Before the rest of the lab can be conducted, one must first install the required packages. In a terminal (I used Powershell), run the following commands:  
```
pip install jdcal
pip install astral
pip install geopy
pip install pytz
pip install psutil
```
Now, the rest of the lab can begin. In order to properly run the examples, the current directory has to be changed. To get into the directory (as found in previous labs), run the following commands:  
```
cd ~\iot
cd lesson3
```
Then, to run any of the examples provided, the following syntax must be used: `python (file)`  

## julian.py
![image](https://github.com/user-attachments/assets/37609e35-ce58-4b1f-a5f7-ddc1ce809180)  
This program simply converts the current calendar date (Gregorian) into the Julian and Modified Julian Calendars.

## date_example.py
![image](https://github.com/user-attachments/assets/7562cac6-a843-4d4c-8d7d-1b3784db6e2b)  
This prints out the current date, followed by the time and day. It also prints out the days until both the First and Last day of classes (at Stevens Institute of Technology)

## datetime_example.py
![image](https://github.com/user-attachments/assets/17f66fc4-ef82-4cae-b961-2bafb7e5f876)  
This script prints the date and time repeatedly, which is accurate to one-thousandth of a milisecond.

## time_example.py
![image](https://github.com/user-attachments/assets/d783ba5c-8465-4dd4-b3ef-da25bdef7006)  
This script will print out the day and time every 10 seconds, until the program is manually stopped.

## sun.py "New York"
![image](https://github.com/user-attachments/assets/9c18a5d6-ec64-4cfc-8b57-8154972397e7)  
This takes a location input by the user and returns the times of dawn, sunrise, noon, sunset, and dusk. It also provides the timezone, and geographical coordinates. This command works for other major cities worldwide.

## moon.py 
![image](https://github.com/user-attachments/assets/16522767-c7c6-403d-bdf9-ab5c6f8cc743)  
This will iterate through the next 30 days, and print the corresponding moon phases for each day in a row.

## coordinates.py "Samuel C. Williams Library"
![image](https://github.com/user-attachments/assets/d7d67e27-b3d3-42b5-aa2a-526ac4fa7fc5)  
This will print the coordinates of the given place. For this example, it gives the coordinates of Samuel C. Williams Library, located on Stevens Institute of Technology's campus.

## address.py "40.74480675, -74.02532861159351"
![image](https://github.com/user-attachments/assets/1342e098-afc2-44e7-bc6c-7f0bde34c1e8)  
This script takes the given coordinates and will return the address that correlates with the given coordinates.

## cpu.py
![image](https://github.com/user-attachments/assets/1af5dd97-324b-4291-9f2a-565123dfdf0a)  
This prints the number of cores and logical CPUs on the computer it is running on, as well as the utilization of each one.

## battery.py
![image](https://github.com/user-attachments/assets/aa5e85e6-78a3-4cb7-9de3-d03ea8076e05)  
This script displays all relevant information regarding the current battery life of the computer. The statistics displayed are percent charged, remaining time (in seconds), and the current charging state.

## documentstats.py document.txt
![image](https://github.com/user-attachments/assets/dd033dd5-68fd-4590-81da-f3b6edab17ec)
This calculates the 10 most common words found in a text file, including their frequencies.

## Notes
* All relevant files can be found on [Prof. Lu's IoT Repository](https://github.com/kevinwlu/iot)

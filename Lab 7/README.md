# Lab 7 - ThingSpeak and Google Sheets
## *"I pledge my honor that I have abided by the Stevens Honor System" -Aidan Ruck*

## Introdution to the Lab
This lab showcases two methods of creating and logging data, one with MathWorks' ThingSpeak, and the other with Google's APIs. ThingSpeak uses the Internet of Things to update charts, while Google APIs allow a user to send incoming data to a Google Sheet.

## Running ThingSpeak
![image](https://github.com/user-attachments/assets/5184cfc2-7b70-4e1a-8fd6-ed2a82825afa)  
As I already had a [MathWorks account](https://thingspeak.mathworks.com), I logged in and created a new channel named "cpu_loop." Within that channel, I created two fields named "cpu_pc" and "memory_available."
Then, I copied the necessary files to my demo folder using `cp ~/iot/lesson7/thingspeak_cpu_loop.py .` and `cp ~/iot/lesson7/thingspeak_feed.py .`
  
After that, I ran the command `python thingspeak_feed.py` to output the measurements from my CPU every minute. You can see some of the statistics it collected below:  
![image](https://github.com/user-attachments/assets/29fa52b4-c23d-405c-a003-d5a460a64ef7)  
NOTE: I cut off the API Key as to not show personal data. I have also since changed it.  

You can also see the data visualization it made below:  
![image](https://github.com/user-attachments/assets/46c03f2c-2de9-4320-9e83-4b8ff0fd5725)  

## Google Sheets
Firstly, I created a new project on [Google Cloud IAM](https://console.cloud.google.com/projectselector2/iam-admin/iam) named cpudata. Then, I went to the APIs section and turned on Google Drive and Google Sheets API. Then, I created a service account key, and saved the .json file.  
After that, I used `pip install -U gspread oath2client` to install Python packages.  
![image](https://github.com/user-attachments/assets/996d010a-5295-4e56-85c8-ea32fd98168d)  
Then, I used the commands `cp ~/iot/lesson3/system_info.py .` and `cp ~/iot/lesson7/cpu_spreadsheet.py .` to move the files into the demo foler. After that, I used the `mv` command to move my API key into the directory. 
![image](https://github.com/user-attachments/assets/3213c196-5f00-4bae-a565-fca2500b3948)  
I then created a new Google Sheet named cpudata, then I shared it to my API service account as an editor. I deleted all rows but the first, and then added the following headers:  
![image](https://github.com/user-attachments/assets/b691fa3b-b288-4f4c-827a-b49e877f0618)  
Then, I had to edit lines in cpu_spreadsheet.py to match my own spreadsheet and API. To do this, I used the `nano` command. I then ran the command `python cpu_spreadsheet.py`, and had my CPU utilization and memory output to the Google Sheet roughly every 10 seconds.  
![image](https://github.com/user-attachments/assets/79480568-377f-4f8f-89e7-aba071b83c14)  
![image](https://github.com/user-attachments/assets/6cf579ee-96b4-4af1-98a5-d43fef4a8338)  

## Notes
* All files can be found on [Prof. Lu's Repository](https://github.com/kevinwlu/iot/tree/master/lesson7)


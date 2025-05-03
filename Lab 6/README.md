# Lab 6 - Node.js and Pystache
### *"I pledge my honor that I have abided by the Stevens Honor System" -Aidan Ruck*

## Introduction to the Lab
This lab teaches both Node.js and Pystache. Node.js is used to create a web server that can be changed on the client side. Pystache, on the other hand, interprets and renders Mustache templates, which is an easy way to generate text from an input.

## Installing Node.js
![image](https://github.com/user-attachments/assets/9cf2ebae-4f6d-4f98-acad-8187c64416b9)  
Installing Node.js is quite easy, and you can download it directly [from their website.](https://nodejs.org/en/download) The command `node -v` will show the current version of Node, while `npm -v` will display the current version of the "Node Package Manager. I used these two to ensure everything was downloaded properly.

## Examples
All of the exmaples are located within the 'lesson6' directory. To get there, I used `cd ~/iot/lesson6`.
1. The first script to try is a program that simply displays "Hello, World!" on a webpage. The command to find this is `node hello-world.js`.
** ![image](https://github.com/user-attachments/assets/cb94b178-4cad-433d-a90d-fa6e67712ccd)  
2. The second example is very similar, but the server side (terminal) will show whenever a user refreshes the page. This example is `node hello.js`.
**![image](https://github.com/user-attachments/assets/807202d1-e80b-4d84-abcb-ef02ccf45739)  
**![image](https://github.com/user-attachments/assets/239a05b3-0755-4c4d-8838-36fe95afddb3)  
3. The last example gives a different output based on how many times the user has refreshed the webpage. On the server (terminal), it displays how many times the page has been refreshed. The command for this one is `node https.js`.
**![image](https://github.com/user-attachments/assets/359ee620-4521-4ad8-8a0d-1e08a515456a)  
**![image](https://github.com/user-attachments/assets/cfc273fb-8fa7-45b3-acf6-0af0e933f133)  

## Installing Pystache
![image](https://github.com/user-attachments/assets/d7667243-d6c3-445b-88b8-08e5791a22b1)  
I installed Pystache using the command `pip install pystache`.

## Checking the Contents
![image](https://github.com/user-attachments/assets/7ac4d621-b255-415c-bb4d-3509f4d447b1)  
First, I printed the contents of each file, to ensure everything was okay. In order to do this, I used the `cat ` command

## Running the Example Program
![image](https://github.com/user-attachments/assets/00e50091-5a37-4006-806d-f3c1ab11bf3f)  
To run this program, I used `python say_hello.py`. The above image showcases that the first line was written by putting the input into the template, and then using Pystache to put the name Alexa in there. The second one, "Hello, World!" is the template from say_hello.mustache. The alst three outputs are a custom template, which displays the template and then outputs with Google and Siri.

## Notes
* All files can be found on [Prof. Lu's Repository](https://github.com/kevinwlu/iot/tree/master/lesson6).

# Lab 8 - Data Analysis
### *"I pledge my honor that I have abided by the Stevens Honor System" -Aidan Ruck*

## Introduction to the Lab
In this lab, we are introduced to many methods of data analysis, using the data that we obtained from Lab 7. Various Python packages are utilized, suh as numPy, sciPy, and MatPlotlib. The programs also used Keras to find a Linear Regression model to predict future values.

## Required Installations
To install the needed packages, I used the command: `pip install -U numpy scipy scikit-learn matplotlib pandas tensorflow keras`.  
![image](https://github.com/user-attachments/assets/34b512bc-a3af-4dee-81e8-ce4881d78156)  
I then ran the first test program, keras_diabetes.py. To do this, I used `python keras_diabetes.py`.  
![image](https://github.com/user-attachments/assets/8685f53c-4d39-4213-927a-f139d91d0285)  
Then I ran the second test program with `python keras_first_network.py`.

## Data Analysis
cpu_spreadsheet.py (from Lab 7) only collects Available Memory, and not temperature, which is what I used. To begin, I went into the demo directory and moved the necessary files to this folder. The commands that I ran were `cp ~/iot/lesson8/plt_final.py .` and `cp ~/iot/lesson8/plt_cv2.py .`. After that, I used the `nano` command to edit all of the information to match the fact that I used Memory (not temperature), but also to match the name of my Laptop.  
![image](https://github.com/user-attachments/assets/d4dbc368-a028-43ad-be75-711fb1b703b6)  
I did the same for both plt_final.py and plt_cv2.py.  
After running both files, you are presented with all of the charts seen below. plt_final.py produces charts comparing the two variables from the CPU usage. The second program, plt_cv2.py, uses scikit-learn to produce a linear regression model. This data is not as linear as temperature, so it is not very accurate.  
![image](https://github.com/user-attachments/assets/80fff4be-6cf6-42ab-9afc-691de5fa1a18)  
![image](https://github.com/user-attachments/assets/6f692518-3a37-457d-8bdc-68312ecb3870)  
![image](https://github.com/user-attachments/assets/b2b92d56-9191-4408-85ab-859b535f70a9)  
![image](https://github.com/user-attachments/assets/e0f88bef-4882-4914-b767-df7af6384a40)  
![image](https://github.com/user-attachments/assets/314447d9-bc0b-43d1-be88-9b503326219b)  
![image](https://github.com/user-attachments/assets/d7fac393-2793-4bb9-87e5-c5ecfa4ff7d4)  
Here are the outputs from plt_cv2.py:  
![image](https://github.com/user-attachments/assets/aec4fc9e-bfba-4a44-a892-21d2e1b8b88e)  

## Notes
* All files can be found on [Prof. Lu's Repository](https://github.com/kevinwlu/iot/tree/master/lesson8)

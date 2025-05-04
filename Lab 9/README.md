# Lab 9 - YANG
### *"I pledge my honor that I have abided by the Stevens Honor System" -Aidan Ruck*

## Introduction to the Lab
This lab teaches us how to use PYANG and PlantUML. PYANG is for creating data schemes, organizing data consistently, and even convert things between different file types such as .yin and .uml. PlantUML is for the latter, making diagrams from .uml files. To install them, I ran `pip install pyang` and `pip install plantuml`

## YANG
I went back into my demo folder (created in previous labs), and copied the YANG file to this directory using the command `cp ~/iot/lesson9/intrustiondetection.yang .`. I then ran the `cat` command to display the file, which gave the following output:  
![image](https://github.com/user-attachments/assets/f1b6f2ec-a865-4aaf-9214-1f51e2713cab)  
Then, I used `pyang intrusiondetection.yang -f yin -o intrusiondetection.yin` to conver it from a YANG file into a YIN file.  
![image](https://github.com/user-attachments/assets/5180ec74-9ea2-4a05-a90f-cf0d6ebb3da1)  
Here are the contents of this file (using `cat`):  
![image](https://github.com/user-attachments/assets/70713394-4b26-4283-afae-8558ac6e29d3)  
Similarly, I then used `pyang intrusiondetection.yang -f uml -o intrusiondetection.uml --uml-no=stereotypes,annotations,typedef` to convert it to a .uml file.  
![image](https://github.com/user-attachments/assets/e9d3aac1-8d0a-4321-badf-548b43a56c45)  

## PlantUML
Then, using PlantUML, I converted the .uml file we just made using the command `python -m plantuml intrusiondetection.uml`. Below is the resulting diagram, which was made into a .png file.  
![intrusiondetection](https://github.com/user-attachments/assets/ff95bed2-1ec1-49d1-a400-3cab7d444bcb)

## Notes
* All files can be found in [Prof. Lu's Repository](https://github.com/kevinwlu/iot/tree/master/lesson9)

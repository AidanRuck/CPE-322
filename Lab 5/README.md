# Lab 5 - Paho-MQTT
### *"I pledge my honor that I have abided by the Stevens Honor System" - Aidan Ruck*

## Introduction to the Lab
This lab is meant to help familiarize with two different implementations of MQTT, which is used for transmitting messages over a given network. This lab utilizes both Mosquitto and Paho-MQTT to send messages between two terminals.

## Installing Mosquitto
As I utilize a Windows machine, I had to first download Moquitto from [it's website.](https://mosquitto.org/download/) Then, I ran the command `git pull` to update my local version.

## Testing Mosquitto
![image](https://github.com/user-attachments/assets/30810583-df39-4fac-977b-65f717cdb5be)  
I then opened two terminals to test if Mosquitto was working. One one terminal, I ran the command `mosquitto_sub -h localhost -v -t test/topic`. On a separate terminal, I attempted to send a message using `mosquitto_pub -h localhost -t test/topic -m "hello world"`. As one can see in the image, the terminal displayed the message from the other terminal.

## Installing Paho
![image](https://github.com/user-attachments/assets/0e0989b6-457b-4ba5-966b-76256140e899)  
First, I ran the command `pip install paho-mqtt`. Then, I cloned the test repository by running the command `git clone https://github.com/eclipse/paho.mqtt.python.git`.

## Paho Examples
1. The first test runs `python sub.py` on one terminal, then `python pub.py` on the other.
** The output from the publish terminal shows the message on the subscriber terminal.
** ![image](https://github.com/user-attachments/assets/2124172a-d389-43c0-9d8a-fef662cb36a1)  
2. The second test is to see what happens when multiple messages are published using the new files `python sub-multiple.py` and `python pub-multiple.py`.
** Both messages will be received by the subscriber as seen.
** ![image](https://github.com/user-attachments/assets/1edeb36d-c326-4a49-847b-dce7beb7e0cc)  
3. The third and final test is continuously printed messages, utilizing the `python subcpu.py` and `python pubcpu.py` commands.
** ![image](https://github.com/user-attachments/assets/ea8488f2-10a5-456e-8395-53872fc80839)  

## Notes
* All files can be found on [Prof. Lu's Repository](https://github.com/kevinwlu/iot/tree/master/lesson5)

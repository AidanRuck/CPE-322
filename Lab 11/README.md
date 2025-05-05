# Lab 11 - Qiskit

## Introduction to the Lab
Qiskit is part of IBM's Quantum Platform, and it stands for Quantum Information Software Kit). It was created by IBM to develop programs that interact with IBM's Quantum Computer, or in a simulated environment (what is happening here).

## Creating an API Token
Before using Qiskit, I had to create an [IBM Account.](https://quantum.ibm.com/)  After doing so, I generated and saved a version of my API key for the test programs I will be running.

## Qiskit Installation
In order to interact with the Quantum Platform, I first have to install the Qiskit packages on my local machine. The command block I ran is below:
```
pip install qiskit[visualization]
pip install qiskit-aer
pip install qiskit_ibm_provider
```

## Qiskit Setup
First, I ran `cd ~/iot/lesson11` to get into the lab's working directory. Then, to connect my account to my bash, I used the following commands (recommended from other students):  
```
winpty python.exe
from qiskit_ibm_provider import IBMProvider
IBMProvider.save_account("API_KEY")
exit()
```

## Qiskit Terra
The first program we are running is qiskit_terra_example.py. The file uses old syntax, so one must go into the package and update the inclusions from `from qiskit import aer ` to `from qiskit_aer import aer`. As well, the `execute` has been replaced with `transpile` so that needed to be edited as well. I did all of those changes utilizing the `nano` command. Then, with the help of a lot of troubleshooting, I added a line to use MatPlotlib to make a drawing of the Quantum Circuit, which can be seen below:  
![image](https://github.com/user-attachments/assets/d0f8aabc-b634-47d5-ad82-f6455b30841d)  
Then, using other student's work as a reference, I started to try to learn about this Quantum Circuit. Within the drawing, there are two quibits and two classical bits (for measuring). q1 goes to the Hadamard gate first, which takes a qubit from a state of 0 or 1 into a superposition (both at the same time). What this does for our program is make them both equally as likely. After the Hadamard gate, q0 and q1 go to the controlled x-gate. What this does is 'entangle' both qubits, making them q1 hold q0's value. **NOTE: I do not study Quantum Computing, and therefore do not know how to explain this better than that**
To see the regular results of this program, I ran `python qiskit_terra_example.py` and received the following output:  
![image](https://github.com/user-attachments/assets/f1b30541-67c1-4ce0-a5b4-2b03a3b2082a)  
![image](https://github.com/user-attachments/assets/2536ab58-9361-49f1-9160-2baa05a0bf8d)  
What this does is run the Quantum Circuit 1024 times, and keep a count of each measured qubit. Each new run of this program will produce a new output since there is a degree of randomness in the program. As '01' or '10' would signify that the two qubits' values did not match, there are no observed for those counts. This would imply that the controlled x-gate did not do its job (making their values match). The Hadamard gate makes it a near 50/50 split, which is why the values seemingly hover around there.

## Qiskit Aer
In order for Aer to work properly, one must install the qiskit_ibm_runtime package. To do so, run the command `pip install qiskit_ibm_runtime`.  

After this, I was unable to get Aer to work after debugging for multiple hours. After installing, uninstalling, fully cleaning the libraries, etc. I still could not get the second example to run.

## Notes
* All files can be found in [Prof. Lu's Repository](https://github.com/kevinwlu/iot/tree/master/lesson11)

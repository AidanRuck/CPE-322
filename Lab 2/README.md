# Lab 2 - Command Line
### *"I pledge my honor that I have abided by the Stevens Honor System." -Aidan Ruck*

## Introduction to the Lab
This lab is to familiarize students with the Command Line, specifically relating to Debian Linux commands (as that is what Raspberry Pis are based on). These commands are integral to working with a Raspberry Pi, and therefore, one should be knowledgeable. Since these are Linux commands, I used a Git Bash terminal for a Simulation of a Linux Environment (as showcased by other students).

## hostname
![image](https://github.com/user-attachments/assets/b8a46097-9c14-4d38-a0bc-d832bda40e93)  
This command does not give the IP or MAC address, but rather the name assigned to the device within the network. This is generally a name chosen (or randomly assigned) when setting up an operating system.

## env
![image](https://github.com/user-attachments/assets/ea791553-4b52-42f9-b160-9f99d76a0746)  
The env command lists all environment variables that have been added to the computer. These variables allow the user of the device to create names for paths that the computer needs to access. This allows the machine to access specific directories or files that are integral to a program's usage. One such example of this comes from installing a programming language, which will have to be added to the PATHS variable.

## ps
![image](https://github.com/user-attachments/assets/77c0f8ca-7767-416b-9443-00181a43d4a4)  
'ps' stands for 'process status." The command displays relevant information with processes that are currently running. In order, each acronym stands for:
* PID: Process ID
* PPID Parent Process ID
* PGID: Process Group ID
* WINPID: Windows Process ID (information that is associated with Task Manager)
* TTY:TeleTYpewriter (What terminal the process is on)
* UID: User ID (of who started the process)
* STIME: Start Time
* COMMAND: Self explanatory (The actual name of the process)

## pwd
![image](https://github.com/user-attachments/assets/78bbc1b4-f450-49b2-894c-b0bc740fdf97)  
pwd stands for Present Working Directory. All this does is tell you the directory that you are currently typing commands into.

## git clone
![image](https://github.com/user-attachments/assets/01861a82-718e-41e6-ad9c-5e79c935943e)  
'git clone' allows you to create a copy of a GitHub repository. For the purpose of this example, I made a clone of [Prof. Lu's Repository](https://github.com/kevinwlu/iot.git)

## cd iot
![image](https://github.com/user-attachments/assets/20adf669-207c-424c-be6b-c12bf7df9571)  
This command dictates "change directory." This allows you to move between file directories (think folders). This image shows me moving into the iot directory.

## ls
![image](https://github.com/user-attachments/assets/9527b388-18e4-499d-a935-3ea16011f70d)  
This command is used to "List fileS." In this example, the files shown are in Prof. Lu's IoT repository.

## cd
![image](https://github.com/user-attachments/assets/496a12fb-9307-4363-956d-cf23f3090841)  
'cd' is used to change the "Current Directory." If you do not specify a directory to move into, it instead returns you to the previous directory. For this example, it moves us out of the IoT directory.

## df
![image](https://github.com/user-attachments/assets/4ee28e32-b8ec-400c-8ed3-3fe860da4376)  
This command is used to show information on the current disk (or hard drive). It stands for "disk free." It will also showcase all connected systems and their files. Some of the information shown is the name of the system, the space used, and what is available to use.

## mkdir demo
![image](https://github.com/user-attachments/assets/b8e9ced5-fa9a-4c56-a5b4-9a247aed9ab3)  
"Make Directory (name)." What this command has done is make a new directory named 'demo.'

## cd demo
![image](https://github.com/user-attachments/assets/45972cff-7c85-4e3b-bc30-31dc99f57c5e)  
Like the cd command showcase above, this has moved me into the new 'demo' directory.

## nano file
![image](https://github.com/user-attachments/assets/aaf1fa96-7c0b-492f-91b4-cd107c1f26ba)  
"nano (file name)" allows you to write text into a file. It is named this way because of the GNU nano text editor, which is very simple in nature.

## cat file
![image](https://github.com/user-attachments/assets/07d7279f-26e6-4232-b3bc-a85e161921e9)  
'cat' or 'concatenate' is a command used to read, display, or otherwise concatenate text files. It prints the contents of the file that you tell it to. In this case, it showcases what I wrote into the file I made in the previous command. The bottom few lines of text after the command is what I wrote.

## cp file file1
![image](https://github.com/user-attachments/assets/ec1a5a55-f75e-4bbe-992a-b35512f2b58c)  
'cp' stands for "copy." It creates a duplicate of the file that you specify. In this case, the new file is named "file1."

## mv file file2
![image](https://github.com/user-attachments/assets/c358142e-d77e-4571-9ad2-57d81fdd4391)  
This command is actually "move," and is used to move or otherwise rename fies. Since the command did not provide a new directory but instead a nem, it stays within the same location but is renamed (in this case to "file2").

## rm file2
![image](https://github.com/user-attachments/assets/a18c3906-24a8-497d-9aa1-1d4121b087b3)  
'rm' is 'remove.' It deletes a specified file. In the example above, I used it to remove the file2 that was created in a previous example. I then used the 'ls' command to showcase that the file specified was, in fact, deleted.

## clear
![image](https://github.com/user-attachments/assets/fc2db9c9-2554-403a-9135-35373e7350d7)  
The 'clear' command simply removes everything that was in-view within the terminal window. As one can see, all previous commands were removed.

## man uname
![image](https://github.com/user-attachments/assets/6ffb2d3d-5438-44d0-a6ec-5533fef05231)  
'man' command stands for 'manual' and would normally provide detailed information of the commands requested. As a reference, 'uname' refers to Unix Name. To use this command regularly, you need the manual database. Instead, I used the command `uname --help` to learn about the uname command.

## uname -a
![image](https://github.com/user-attachments/assets/72a44918-e60b-443d-a87b-1543ddf1dec3)  
This command prints the system informatiom. The -a option prints "All" available information.

## ifconfig
![image](https://github.com/user-attachments/assets/e469ff24-2abc-472d-802f-a2b167bbafcd)  
'ifconfig' is used to show details about the network interfaces. Since this is used for Unix-based systems, my Windows machine was unable to run it. Because of this, I ran the `ipconfig` command, which is the same command, but for Windows.

## ping localhost
![image](https://github.com/user-attachments/assets/8d0fd182-b86f-42dd-9aa8-c48f40748eed)  
The 'ping' command allows a machine to send test packets to see if a network connection is stable and properly functioning. Since, in this case, it is being sent to localhost (contained on the same machine), the packets are sent from the computer back to the same computer. This can be used to test the performance of the device.

## netstat
![image](https://github.com/user-attachments/assets/9cbf2edf-f63e-4594-be50-64dc1722433b)  
'netstat' is short for "Network Statistics" and it displays current connections to whatever Wi-Fi (or ethernet) connection the computer has. It displays information such as the type of protocol, the IP address, and the current state of all network connections.

## Notes
* As I specified earlier, these were conducted on a Git Bash terminal to simulate a Linux Environment. These commands can be run on some Windows terminals, though they may not function the same way.
* Git Bash is also not a full Unix-based system (like MacOS or Linux Distributions).

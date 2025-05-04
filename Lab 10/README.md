# Lab 10 - Blockchain
### *"I pledge my honor that I have abided by the Stevens Honor System" -Aidan Ruck*

## Introduction to the Lab
This lab teaches about Hashing algorithms (used to secure and verify data) as well as the Blockchain. The blockchain uses a series of algorithms and mathematics to obscure data, and provide a decentralized currency that can be used to keep track of multiple kinds of data.

## Hashing
Hashing is a technique that can be applied to any form of data for security and verification. Once data has been hashed, however, it cannot be returned to its original form. Once I was in the /lesson10/ (`cd ~/iot/lesson10`) directory, I ran the `cat hash_value.py` command to take a peek inside the contents of the file. The content can be found below:  
![image](https://github.com/user-attachments/assets/68a142e6-b799-4a55-8271-ee91ddb41cd0)  
As seen above, this file uses semi random hashing, which is extra secure. I have run it twice such that the difference can be seen.  
![image](https://github.com/user-attachments/assets/461d8cf5-34af-484c-bd04-4750a97cbc63)  

## Blockchain
![image](https://github.com/user-attachments/assets/4e154d31-b8da-414f-bb23-0110b2cd293d)  
We are given the example `snakecoin.py`. When running this command, 20 blocks are added onto the chain with unique hashes. This is an example of an incredibly simply blockchain.  
This creation of a blockchain is further expanded with the file snakecoin-server-full-code.py. This file uses a network, allowing someone to 'mine' blocks via an internet connection.  
![image](https://github.com/user-attachments/assets/67cc9d43-cf88-45cf-a8e6-483293163fb6)  
After running this on one terminal, I opened a second terminal to mine. In order to do this, I used the following commands:  
```
$ curl "localhost:5000/txion" \
     -H "Content-Type: application/json" \
     -d '{"from": "akjflw", "to":"fjlakdj", "amount": 3}'
$ curl localhost:5000/mine
```  
![image](https://github.com/user-attachments/assets/f0c9f698-cb89-4f91-9833-b530d1921c8e)  
After running these commands, the output in the terminal indicates that a block has been mined.  
![image](https://github.com/user-attachments/assets/1aef7864-914f-43d6-9dc0-a03006f097c6)  
As seen on the server-side terminal, the same transactions appear.  
![image](https://github.com/user-attachments/assets/be8a20ec-fa91-46b5-b3e4-cbe678454f89)  
They can also be found at [http://127.0.0.1:50000](127.0.0.1:50000).

## Python Blockchain App
![image](https://github.com/user-attachments/assets/7c35eb02-90b6-474b-bba7-5a4196c57b09)  
According to the Lab instructions, I first cloned [Satwik Kansals' Repository](https://github.com/satwikkansal/python_blockchain_app) using `git clone https://github.com/satwikkansal/python_blockchain_app.git` After doing so, I used `cd` to navigate into the directory, and then the `nano node_server.py` command to uncomment the last line of the file. This allows a port to run.  
![image](https://github.com/user-attachments/assets/9e8b0bfa-779f-493e-b5a7-dcef8d8849cf)  
After this, I ran the server using `python node_server.py`. On a new terminal, I ran the app with `python run_app.py` on a new terminal window. Going to [http://127.0.0.1:50000](127.0.0.1:5000) shows a page which allows the user to mine blocks.  
![image](https://github.com/user-attachments/assets/f7fb28fc-77a3-49f9-9e09-2d65e4a90266)  
![image](https://github.com/user-attachments/assets/2803536b-e47d-4e71-bc28-ffc81fb56935)  
After filling the form out, posting it, and then requesting to mine, the transaction becomes present at [http://127.0.0.1:8000/mine](127.0.0.1:8000/mine)

## Notes
* All files can be found on [Prof. Lu's Repository](https://github.com/kevinwlu/iot/tree/master/lesson10)

# Importing Library and creating Socket Instance
import socket
s = socket.socket()
  
# Defining Port 
port = 5056                
  
s.connect(('127.0.0.1', port)) 
  
# Receving data from server (buffer)
recievs_data = s.recv(1024) 

print(recievs_data.decode())

s.close()     

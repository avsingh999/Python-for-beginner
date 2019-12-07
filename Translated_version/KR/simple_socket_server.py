# Importing Library and creating Socket Instance
import socket                
s = socket.socket()          
print ("Socket successfully created")

#Port
port = 5056                
  
s.bind(('127.0.0.1', port))          

#It can listen upto 5 connection
s.listen(5)      
print ("socket is listening" )           

while True: 
  
   c, addr = s.accept()      
   print ('Got connection from', addr )
  
   c.send('Thank you for connecting'.encode())
  
   c.close() 

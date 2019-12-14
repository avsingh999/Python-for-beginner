# 라이브러리 가져오기 및 소켓 인스턴스 작성
import socket
s = socket.socket()
  
# port 정의하기 
port = 5056                
  
s.connect(('127.0.0.1', port)) 
  
# 서버로부터 데이터 받기(버퍼)
recievs_data = s.recv(1024) 

print(recievs_data.decode())

s.close()     

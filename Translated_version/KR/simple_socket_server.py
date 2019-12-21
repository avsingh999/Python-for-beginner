# 라이브러리 가져 오기 및 소켓 인스턴스 작성
import socket                
s = socket.socket()          
print ("소켓이 성공적으로 만들어졌습니다.")

# 포트
port = 5056                
  
s.bind(('127.0.0.1', port))          

# 최대 5개의 연결을 들을 수 있습니다
s.listen(5)      
print ("소켓이 듣는중입니다." )           

while True: 
  
   c, addr = s.accept()      
   print ('다음 주소로부터 연결을 가져오는중 :', addr )
  
   c.send('연결해주셔서 감사합니다.'.encode())
  
   c.close() 

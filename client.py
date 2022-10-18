import socket, sys

class Client:
    BUFFSIZE = 1024
    def __init__(self, addr):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(addr)
    
    def mainloop(self):
        while True:
            self.socket.send(input('>>>').encode('utf-8'))
            data = self.socket.recv(Client.BUFFSIZE).decode('utf-8')
            if data:
                print(data)
            else:
                break

def main():
    args = sys.argv[1:]
    serv = Client((args[0], int(args[1])))
    serv.mainloop()


main()
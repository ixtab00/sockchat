import socket, sys
from typing import Tuple


class Server:
    BUFFSIZE = 1024
    def __init__(self, addr: Tuple) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(addr)
    
    def listen(self, max_num: int) -> None:
        self.socket.listen(max_num)

    def mainloop(self) -> None:
        while True:
            sock, addr = self.socket.accept()
            while True:
                data = sock.recv(Server.BUFFSIZE)
                if data:
                    print(data.decode('utf-8'))
                    sock.send(input('>>>').encode('utf-8'))
                else:
                    sock.close()
                    break

def main():
    args = sys.argv[1:]
    serv = Server((args[0], int(args[1])))
    serv.listen(int(args[2]))
    serv.mainloop()


main()
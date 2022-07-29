from audioop import add
import socket

class netsock:

    _hostname = ''

    def __init__(self,port):
        self._port = port
        self._hostname = socket.gethostbyname()
    

    def buildSocket(self,address=_hostname) -> socket:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.bind(address, self._port)


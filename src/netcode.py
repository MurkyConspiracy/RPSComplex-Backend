import socket
from loclogger import lprint

class netsock:

    def __init__(self,port):
        lprint('Start netsock constructor')
        self._port = port
        self._hostname = socket.gethostname()
        self._buildSocket()
    

    def _buildSocket(self,) -> socket:
        lprint('Build socket')
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        lprint('Binding..')
        sock.bind((self._hostname,self._port))
        sock.listen(11)
        lprint('Socket established')
        return sock


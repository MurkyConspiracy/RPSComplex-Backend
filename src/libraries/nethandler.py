import socket
from libraries.loghandler import lprint
import threading



class netsock:

    def __init__(self,port):
        self._port = port
        self._hostname = socket.gethostname()
        self._socket = self._buildSocket()
        netthread = threading.Thread(target=self._listen)
        netthread.start()
    
    def _buildSocket(self):
        lprint('Build socket')
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        lprint('Binding..')
        sock.bind((self._hostname,self._port))
        lprint('Socket established')
        return sock

    def _listen(self):
        lprint('Starting to listen...')
        self._socket.listen(11)
        lprint('Waiting for data...')
        conn, addr = self._socket.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                lprint(str(data))
                conn.send("Data Rec: " + str(data),'UTF-8')
                lprint("Data sent back!")
        lprint('End Listen...')
        self._listen()
                

    


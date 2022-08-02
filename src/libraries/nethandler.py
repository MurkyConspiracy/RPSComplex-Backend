import socket
from libraries.loghandler import lprint
import threading


#OOP class for defining a socket object -> netsock
#This class will handle all inbound requests from the Frontend and send data to the Database
class netsock:

    #Object constructor with network port as paramater
    #Grabs bound IP address and assigns it
    #Creates a socket connection and starts that as a process on a new thread
    def __init__(self,port):
        self._port = port
        self._hostname = socket.gethostname()
        self._socket = self._buildSocket()
        netthread = threading.Thread(target=self._listen)
        netthread.start()
    
    #Creates the TCP/IP socket and binds it to the defined port on the address
    #Will need to make moduler if binding to an external IP via NATing
    def _buildSocket(self):
        lprint('Build socket')
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        lprint('Binding..')
        sock.bind((self._hostname,self._port))
        lprint('Socket established')
        return sock

    #Starts the socket listening and gives it 11 (arbitrary) concurrent connections
    #Waits for incoming data and echos it out. This is all in strings, will need to convert to bytes
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
                

    


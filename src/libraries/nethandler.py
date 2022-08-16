import socket, threading
from libraries.loghandler import lprint
from libraries.datahandler import handleTCPRequest
import libraries.confighandler


def startNetProc():

    _port = libraries.confighandler.getPort()
    _hostname = socket.gethostname()

    lprint('Build socket')
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    lprint('Binding...')
    sock.bind((_hostname,_port))
    lprint('Socket established',1)

    lprint('Starting network thread!',1)
    netthread = threading.Thread(target=_listen,args=[sock])
    netthread.start()

#Starts the socket listening and gives it 11 (arbitrary) concurrent connections
#Waits for incoming data and echos it out. This is all in strings, will need to convert to bytes

def _listen(sock):
    lprint('Starting to listen...')
    sock.listen(11)
    lprint('Waiting for data...',1)
    conn, addr = sock.accept()
    with conn:
        while True:
            try:
                data = conn.recv(1024)
            except ConnectionResetError:
                _listen(sock)
                lprint('Connection Reset! Exiting current connection')
                return
            except KeyboardInterrupt:
                raise
            if not data:
                break
            lprint(str(data))
            packetResponse = handleTCPRequest(data)
            lprint(packetResponse)
            conn.send(packetResponse[2])
    lprint('End Listen...')
    _listen(sock)
                    

    


from libraries import *
from libraries.nethandler import netthread
from libraries.loghandler import lprint

def main():
        
        libraries.confighandler.loadConfig()
        netConnection = netthread(libraries.confighandler.getPort())
        lprint('Packet test pass:\t{0}'.format(str(libraries.datahandler.testPackerRouting())))

if __name__ == "__main__":
                main()
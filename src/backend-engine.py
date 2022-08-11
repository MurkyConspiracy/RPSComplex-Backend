from libraries import confighandler, datahandler, loghandler, nethandler

def main():
        
        confighandler.loadConfig()
        netConnection = nethandler.netthread(confighandler.getPort())
        loghandler.lprint('Packet test pass:\t{0}'.format(str(datahandler.testPackerRouting())))

if __name__ == "__main__":
                main()
from libraries import confighandler, datahandler, loghandler, nethandler

def main():
        
        confighandler.loadConfig()
        loghandler.lprint('Testing known good packets:\t{0}'.format(str(datahandler.testPackerRouting())),1)
        nethandler.startNetProc()

if __name__ == "__main__":
                main()
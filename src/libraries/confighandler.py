import logging, libraries.confighandler, tomli, sys, os

global config_dict
config_dict = {}

def loadConfig():
    try:
        with open("config/ServerConfig.toml", "rb") as configfile:
            config_dict.update(tomli.load(configfile))
        if(libraries.confighandler.getPrintDebug()):
            logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
        else:
            logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
        from libraries.loghandler import lprint
        lprint("Config loaded!")
    except tomli.TOMLDecodeError:
        lprint("Config Invalid! Check syntax and try again!",3)
        sys.exit()
    except FileNotFoundError:
        createConfig()
        from libraries.loghandler import lprint
        if(libraries.confighandler.getPrintDebug()):
            logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
        else:
            logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
        from libraries.loghandler import lprint
        lprint("Config loaded!")

def createConfig():
    from libraries.loghandler import lprint
    import os
    if(not os.path.exists('config')):
        os.mkdir('config')
    defaultconfig = '''title = "RPSComplex-Backend Config"

    [owner]
    name = "Nicholas Reeder"

    [database]
    server = "172.17.0.3"
    port = 1433
    enabled = 0

    [server]
    port = 6666
    printdebuglog = 1'''

    with open('config/ServerConfig.toml', mode='w+') as configfile:
        configfile.write(defaultconfig)
    with open('config/ServerConfig.toml', mode='rb') as configfile:
        config_dict.update(tomli.load(configfile))
        

def getPort():
    return config_dict["server"]["port"]

def getPrintDebug():
    return config_dict["server"]["printdebuglog"]
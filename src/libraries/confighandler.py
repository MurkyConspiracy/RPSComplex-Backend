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
        lprint("Config Invalid! Check syntax and try again!")
        sys.exit()
    except FileNotFoundError:
        createConfig()
        lprint("Config loaded!")

def createConfig():
    from libraries.loghandler import lprint
    import os
    lprint(os.getcwd())
    for file in os.listdir(os.getcwd()):
        lprint(file)

def getPort():
    return config_dict["server"]["port"]

def getPrintDebug():
    return config_dict["server"]["printdebuglog"]
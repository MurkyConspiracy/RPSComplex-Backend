from distutils.command.config import config
from glob import glob
import tomli, sys
from libraries.loghandler import lprint

global config_dict
config_dict = {}

def loadConfig():
    try:
        with open("config/ServerConfig.toml", "rb") as configfile:
            config_dict.update(tomli.load(configfile))
        lprint("Config loaded!")
    except tomli.TOMLDecodeError:
        lprint("Config Invalid! Check syntax and try again!")
        sys.exit()
    except FileNotFoundError:
        createConfig()
        lprint("Config loaded!")

def createConfig():
    import os
    lprint(os.getcwd())
    for file in os.listdir(os.getcwd()):
        lprint(file)

def getPort():
    return config_dict["server"]["port"]

def getPrintDebug():
    return config_dict["server"]["printdebuglog"]
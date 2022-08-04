from urllib.request import DataHandler
from libraries import *
from libraries.nethandler import netsock

netConnection = netsock(6666)
libraries.loghandler.lprint('Start packet test:\t{0}'.format(str(libraries.datahandler.testPackerRouting())))
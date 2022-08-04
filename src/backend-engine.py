from libraries import *
from libraries.nethandler import netsock

netConnection = netsock(6666)
libraries.loghandler.lprint('Packet test pass:\t{0}'.format(str(libraries.datahandler.testPackerRouting())))
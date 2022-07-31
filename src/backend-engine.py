import sys, os
sys.path.insert(0,os.getcwd() + '/libraries')
from libraries.nethandler import *

netConnection = netsock(6666)

print('done')
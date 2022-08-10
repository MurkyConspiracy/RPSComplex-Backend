import datetime
from threading import Semaphore
screenlock = Semaphore(1)



#This is trash I guess, going to work with Caleb to understand how to log like a man
class LLevel:
        DEBUG = 0
        LOG = 1
        ERROR = 2

#Figure out how to use config in here without circular imports.....
def lprint(text,level=LLevel.DEBUG):
    if(level == LLevel.DEBUG):
        screenlock.acquire()
        print(str(datetime.datetime.now()) + '\t <DEBUG> \t' + str(text))
        screenlock.release()
    elif(level == LLevel.LOG):
        screenlock.acquire()
        print(str(datetime.datetime.now)() + '\t' + text)
        screenlock.release()
    elif(level == LLevel.ERROR):
        screenlock.acquire()
        print(str(datetime.datetime.now()) + '[ERROR START]\n\n' + text + '\n\n[ERROR END]')
        screenlock.release()
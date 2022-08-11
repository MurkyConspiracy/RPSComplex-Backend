import datetime, logging, os, libraries.confighandler
from ntpath import basename
from inspect import stack
from threading import Semaphore
screenlock = Semaphore(1)

#This is trash I guess, going to work with Caleb to understand how to log like a man
class LLevel:
        DEBUG = 0
        INFO = 1
        WARN = 2
        ERROR = 3

#Figure out how to use config in here without circular imports.....
def lprint(text,level=LLevel.DEBUG):
    if(level == LLevel.DEBUG):
        screenlock.acquire()
        log = logging.getLogger(basename(stack()[1][1]))
        log.debug(str(text))
        screenlock.release()
    elif(level == LLevel.INFO):
        screenlock.acquire()
        log = logging.getLogger(basename(stack()[1][1]))
        log.info(str(text))
        screenlock.release()
    elif(level == LLevel.WARN):
        screenlock.acquire()
        log = logging.getLogger(basename(stack()[1][1]))
        log.warning(str(text))
        screenlock.release()
    elif(level == LLevel.ERROR):
        screenlock.acquire()
        log = logging.getLogger(basename(stack()[1][1]))
        log.error(str(text))
        screenlock.release()
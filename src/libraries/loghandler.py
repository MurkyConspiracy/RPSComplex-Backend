import datetime

#This is trash I guess, going to work with Caleb to understand how to log like a man
class LLevel:
        DEBUG = 0
        LOG = 1
        ERROR = 2

def lprint(text,level=LLevel.DEBUG):
    if(level == LLevel.DEBUG):
        print(str(datetime.datetime.now()) + '\t <DEBUG> \t' + text)
    elif(level == LLevel.LOG):
        print(str(datetime.datetime.now)() + '\t' + text)
    elif(level == LLevel.ERROR):
        print(str(datetime.datetime.now()) + '[ERROR START]\n\n' + text + '\n\n[ERROR END]')
from doctest import OutputChecker
import json
from tokenize import String
from libraries.loghandler import lprint
#File Header to know where to start parsing data
_HEADER = (b'RPS')

#File Footer to know where the file end
_FOOTER = (b'COMPLEX')

#Request sample
#Request Header (3 Bytes):
    #82, 80, 83

#Request ID (1 Byte)
    #XX

#Request Data length (4 Bytes):
    #XX, XX, XX, XX

#Data (Request Length Bytes)
    #XX, .. .. .. .. XX, ..
 
#Request Footer (7 Bytes):
    #43, 4f, 4d, 50, 4c, 45, 58

#I don't think I will ever use data length in code; however, I thinkg it might be useful
#It also acts as a way for me to verify request length. 

RequestDict = {}

def formatPacket(data: any, packetType: int):
    outPacket = bytearray(_HEADER)
    if packetType > 255 or packetType < 0:
        raise ValueError('Invalid int!')
    outPacket.append(packetType)
    outPacket.extend(len(data).to_bytes(4, byteorder="big"))
    try:
        outPacket.extend(data)
    except TypeError:
        outPacket.extend(str(data).encode('utf-8'))
    
    outPacket.extend(_FOOTER)
    return outPacket
    
    
def handleTCPRequest(packetData) -> tuple:
    if packetData[:3] != _HEADER:
        lprint("Failed Header check:\nControl:\t{0}\nInput:\t\t{1}".format(_HEADER,packetData[:3]),2)
        return (False,"?",formatPacket(f'{{"status":"failed","reason":"Failed header check"}}',255))
    elif packetData[len(packetData)-7:] != _FOOTER:
        lprint("Failed Footer check:\nControl:\t{0}\nInput:\t\t{1}".format(_FOOTER,packetData[len(packetData)-7:]),2)
        return (False,"?",formatPacket(f'{{"status":"failed","reason":"Failed footer check"}}',255))
    elif str(int(packetData[3])) not in RequestDict:
        lprint("Failed Type Check:\nType:\t{0}".format(int(packetData[3])),2)
        return (False,"?",formatPacket(f'{{"status":"failed","reason":"Failed packet ID check"}}',255))
    elif int.from_bytes(packetData[4:8],byteorder='big') != len(packetData[8:len(packetData)-7]):
        lprint(f"Failed Length Check:\nLength Recived: {int.from_bytes(packetData[4:8],byteorder='big')}\nReal Length: {len(packetData[8:len(packetData)-7])}",2)
        return (False,str(RequestDict[str(packetData[3])].__qualname__),formatPacket(f'{{"status":"failed","reason":"Failed packet length check"}}',255))
    else:
        resultdata = RequestDict[str(packetData[3])](packetData[8:len(packetData)-7])
        return (True,"Packet Routed!", resultdata)


def testPacketData(data) -> bytearray:
    lprint(f'Packet Data output: {data}')
    return(formatPacket(f'{{"status":"passed"}}', 127))
RequestDict["0"] = testPacketData

def createUserPacket(data) -> bytearray:
    try:
        userDataDict = json.loads(data)
    except json.JSONDecodeError:
        return formatPacket(f'{{"status":"Malformed User Data"}}', 128)
    lprint(userDataDict)
    #Need to test this, this might need to be a try except block. I am not sure if userDataDict[] will return None or an exception
    if(userDataDict['username'] is None or userDataDict['email'] is None):
        return formatPacket(f'{{"status":"Malformed User Data"}}', 128)
    #Need to create data handling with a database next.
    return formatPacket(f'{{"status":"passed","reason":"Account Created"}}',128)
RequestDict["1"] = createUserPacket


#Test Packet section, need to implement this to use netcode to test. This will only test logic for now!
def testPackerRouting() -> String:
    try:
        lprint('Loading known good packet.')
        __TESTPACKET_TEST = bytearray([0x52,0x50,0x53,0x00,0x00,0x00,0x00,0x03,0x52,0x50,0x53,0x43,0x4f,0x4d,0x50,0x4c,0x45,0x58]) 
        lprint(__TESTPACKET_TEST.decode('utf-8'))
        lprint("Test Packet Output: " + str(handleTCPRequest(__TESTPACKET_TEST)))
        lprint('Loading known good packet.')
        __TESTPACKET_ACCOUNTCREATE = formatPacket('{"username": "testing", "email": "test@test.org"}', 1) 
        lprint(__TESTPACKET_ACCOUNTCREATE.decode('utf-8'))
        lprint("Test Packet Output: " + str(handleTCPRequest(__TESTPACKET_ACCOUNTCREATE)))
        return 'Pass'
    except Exception as e:
        import os, sys
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        lprint(f'Error: {exc_type} fname: {fname} line: {exc_tb.tb_lineno}')
        return 'Fail'

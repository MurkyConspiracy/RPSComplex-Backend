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


def handleTCPRequest(packetData) -> tuple:
    if packetData[:3] != _HEADER:
        lprint("Failed Header check:\nControl:\t{0}\nInput:\t\t{1}".format(_HEADER,packetData[:3]))
        return (False,"?","Header Check Failed!")
    elif packetData[len(packetData)-7:] != _FOOTER:
        lprint("Failed Footer check:\nControl:\t{0}\nInput:\t\t{1}".format(_FOOTER,packetData[len(packetData)-7:]))
        return (False,"?","Footer Check Failed!")
    elif str(int(packetData[3])) not in RequestDict:
        lprint("Failed Type Check:\nType:\t{0}".format(int(packetData[3])))
        return (False,"?","Packed ID not found!")
    elif int.from_bytes(packetData[4:8],byteorder='big') != len(packetData[8:len(packetData)-7]):
        lprint("Failed Length Check:\nLength Recived")
        return (False,str(RequestDict[str(packetData[3])].__qualname__),"Packet Length mismatch!")
    else:
        resultdata = RequestDict[str(packetData[3])](packetData[8:len(packetData)-7])
        return (True,"Packet Routed!", resultdata)


def testPacketData(data) -> bytearray:
    lprint('Packet Data output: {0}'.format(data))
    return(data)
RequestDict["1"] = testPacketData

def createUserPacket(data) -> bytearray:
    lprint
RequestDict["2"] = createUserPacket



#Test Packet section!
def testPackerRouting() -> bool:
    try:
        lprint('Loading known good packet.')
        __TestPacket = bytearray([0x52,0x50,0x53,0x01,0x00,0x00,0x00,0x03,0x52,0x50,0x53,0x43,0x4f,0x4d,0x50,0x4c,0x45,0x58]) 
        lprint(__TestPacket.decode('utf-8'))
        lprint("Test Packet Output: " + str(handleTCPRequest(__TestPacket)))
        return True
    except:
        return False


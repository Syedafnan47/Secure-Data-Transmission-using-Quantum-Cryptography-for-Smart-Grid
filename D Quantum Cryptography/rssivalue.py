import random
from random import randint
def __init__(self, addr):
    self.addr = addr
    self.hci_sock = bt.hci_open_dev()
    self.hci_fd = self.hci_sock.fileno()
    self.bt_sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
    self.bt_sock.settimeout(10)
    self.connected = False
    self.cmd_pkt = None

def prep_cmd_pkt(self):
    """Prepares the command packet for requesting RSSI"""
    reqstr = struct.pack(
        "6sB17s", bt.str2ba(self.addr), bt.ACL_LINK, "\0" * 17)
    request = array.array("c", reqstr)
    handle = fcntl.ioctl(self.hci_fd, bt.HCIGETCONNINFO, request, 1)
    handle = struct.unpack("8xH14x", request.tostring())[0]
    self.cmd_pkt = struct.pack('H', handle)

def connect(self):
    """Connects to the Bluetooth address"""
    self.bt_sock.connect_ex((self.addr, 1))  # PSM 1 - Service Discovery
    self.connected = True

def get_rssi(self):
    """Gets the current RSSI value.
    @return: The RSSI value (float) or None if the device connection fails
             (i.e. the device is nowhere nearby).
    """
    try:
        # Only do connection if not already connected
        if not self.connected:
            self.connect()
        if self.cmd_pkt is None:
            self.prep_cmd_pkt()
        # Send command to request RSSI
        rssi = bt.hci_send_req(
            self.hci_sock, bt.OGF_STATUS_PARAM,
            bt.OCF_READ_RSSI, bt.EVT_CMD_COMPLETE, 4, self.cmd_pkt)
        rssi = struct.unpack('b', rssi[3])[0]
        return rssi
    except IOError:
        # Happens if connection fails (e.g. device is not in range)
        self.connected = False
        return None
    
def rssimodel(mxnodes):
    temp1=[]
    for i in range(1,mxnodes):
        rssi1=round(randint(50, 99))
        rssi2=round(randint(50, 99))
        rssi3=round(randint(50, 99))
        rssi4=round(randint(50, 99))
        rssi5=round(randint(50, 99))
        rssi6=round(randint(50, 99))
        rssi7=round(randint(50, 99))
        rssi8=round(randint(50, 99))
        temp2=[]
        temp2.append(i)
        temp2.append("-"+str(rssi1))
        temp2.append("-"+str(rssi2))
        temp2.append("-"+str(rssi3))
        temp2.append("-"+str(rssi4))
        temp2.append("-"+str(rssi5))
        temp2.append("-"+str(rssi6))
        temp2.append("-"+str(rssi7))
        temp2.append("-"+str(rssi8))
        temp1.append(temp2)
    return temp1

def residuals(p, d, x):
    A, B, C = p
    err = d - (A * x**B + C)
    return err



def peval(x, p):
    return p[0] * x**p[1] + p[2]

def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


#test=rssimodel()
#print(test)

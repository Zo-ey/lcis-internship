from enum import Enum

BROADCAST = -1

WSNMessageType = Enum("WSNMessage", ("Data", "Advertisement"))

class WSNMessage:
    def __init__(self, src=None, dest=None, message_type=None, data=None):
        self.src = src
        self.dest = dest
        self.type = WSNMessageType[message_type]
        self.data = data
    
    def __str__(self):
        ret = 'src : '+str(self.src) + ", "
        ret += 'dest : '+str(self.dest) + ", "
        ret += 'message_type : '+str(self.type) + ", "
        ret += 'data : '+str(self.data)
        return ret

    def __eq__(self, other):
        return isinstance(other, WSNMessage) and\
                all([getattr(self, attr) == getattr(other, attr) for attr in vars(self)])

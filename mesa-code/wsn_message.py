from enum import Enum

BROADCAST = -1

WSNMessageType = Enum("WSNMessage", ("Data", "Advertisement"))

class WSNMessage:
    def __init__(self, src=None, dest=None, message_type=None, data=None):
        self.src = src
        self.dest = dest
        self.type = WSNMessageType[message_type]
        self.data = data

    def __eq__(self, other):
        return isinstance(other, WSNMessage) and\
                all([getattr(self, attr) == getattr(other, attr) for attr in vars(self)])

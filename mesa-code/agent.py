from enum import Enum

from mesa import Agent

from wsn_message import WSNMessageType as MT


State = Enum("State", ("Safe", "Suspicious", "Blackhole"))
# Ideas/TODO:
# * if suspicious for a too long time, then blackhole. Time checked with time the program has been
#   running or sub between 1st and last timestamp
# * Lying advert: advert with wrong data which is shorter than in reality
# * Not forwarding
# * Pb: How to update messages? 
# * How to check others? -> Since there is no way in Mesa to have comm between agent, the best way
# would be to check other's messages the same way ish that agent check their own and to say if they
# are suspicious. The dt would then count how many agent (including th eagent itself) think that
# "this" agent is suspicious/is a blackhole.

# if the node sent an advertisement of value 0, it's malicious
def is_malicious_ad(m):
    if m.type == MT.Advertisement and m.data == 0:
        return True
    return False

# if the node doesn't send message, it's suspicious
def is_sending_msg(messages):
    for m in messages:
        if m.type == MT.Data:
            return True
    return False

# if the node doesn't forward a msg as expected, it's suspicious (maybe it didn't had the time to
# send it yet)
#def is_forwarding_msg(messages):

# Blackhole if:
# * advert with 0 hops / zero-distance
def update_tags(tags, ownId, fromMe, toMe, throughMe):
    for m in toMe + throughMe:
        if is_malicious_ad(m):
            tags[m.src] = State.Blackhole
    if not(is_sending_msg(fromMe)):
        tags.update({ownId: State.Suspicious})
    return tags

class WSNAgent(Agent):
    def __init__(self, unique_id, model, color):
        super().__init__(unique_id, model)
        self.color = color
        self.fromMe = [] # Messages sent by me
        self.toMe = [] # Messages sent to me
        self.throughMe = [] # Messages sent through me
        self.tagDict = {self.unique_id: State.Safe}
   # Update (and sort) messages lists
    def update_messages(self, messages):
        print("agent "+str(self.unique_id))
        for m in messages:
            print("    ",end="")
            print(m)
            if m.src == self.unique_id:
                self.fromMe.append(m)
            elif m.dest == self.unique_id:
                self.toMe.append(m)
            else:
                self.throughMe.append(m)

    def step(self):
        self.tagDict = update_tags(self.tagDict, self.unique_id, self.fromMe, self.toMe, self.throughMe)
        for id in self.tagDict.keys():
            if self.tagDict[id] != State.Safe:
                print(f"Node {id} is {self.tagDict[id]}")


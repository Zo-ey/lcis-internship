from enum import Enum

from mesa import Agent


State = Enum("State", ("Safe", "Suspicious", "BlackHole"))


class AgentVanet(Agent):
    def __init__(self, unique_id, model, color):
        super().__init__(unique_id, model)
        self.color = color
        self.fromMe = [] # Messages sent by me
        self.toMe = [] # Messages sent to me
        self.transit = [] # Messages sent through me
        self.tag = State.Safe
    
    def update_messages(self, messages):
        for m in messages:
            if m["src"] == self.unique_id:
                self.fromMe.append(m)
            elif m["dest"] == self.unique_id:
                self.toMe.append(m)
            else:
                self.transit.append(m)

    # if the node sent an advertisement of value 0, it's malicious
    def has_malicious_ad():
        for m in self.fromMe:
            if m["type"] == "ad" and m["value"] == 0:
                return True
        return False

    # if the node doesn't send message, it's suspicious
    def is_sending_msg():
        return len(self.fromMe) != 0

    def step(self):
        pass
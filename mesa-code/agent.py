from mesa import Agent

class AgentVanet(Agent):
    def __init__(self, identifier, msgs):
        self.identifier = identifier
        self.fromMe = [] # Messages sent by me
        self.toMe = [] # Messages sent to me
        self.transit = [] # Redirected messges
        self.tag = "safe"
        for m in msgs:
            if m[src] == self.identifier:
                self.fromMe.append(m)
            else if m[dest] == self.identifier:
                self.toMe.append(m)
            else:
                self.transit.append(m)

    # if the node sent an advertisement of value 0, it's malicious
    def has_malicious_ad():
        for m in self.fromMe:
            if m[type] == "ad" and m[value] == 0:
                return True
        return False

    # if the node doesn't send message, it's suspicious
    def is_sending_msg():
        return len(self.fromMe) != 0

    def get_tag(self):
        return self.tag

    def step(self):
        pass

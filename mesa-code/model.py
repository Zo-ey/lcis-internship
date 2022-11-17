import time
import importlib
from mesa import Model
from mesa.space import SingleGrid
#from mesa.space import place_agent
from mesa.time import RandomActivation
from agent import AgentVanet


def split_on_last(string, char):
    rev_string = string[::-1]   # `[::-1]` gets the reverse of string
    end, start = rev_string.split(char, 1)
    return start[::-1], end[::-1]


class ModelVanet(Model):
    def __init__(self, model, agents):
        # Initialize the RNG
        self.seed = model.get("seed")
        if self.seed is None:
            self.seed = time.time()
        self.reset_randomizer(self.seed)
        # Initialize the model
        self.running = True
        self.grid = SingleGrid(model.get("width"), model.get("height"), False) # TODO: here
        self.schedule = RandomActivation(self)
        # Add agents
        for agent_class, agents in agents.items():
            module_name, class_name = split_on_last(agent_class, '.')
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name)
            for agent in agents:
                a = cls(agent["id"], self)#, agent["color"])
                self.schedule.add(a)
                self.grid.place_agent(a, (agent["x"], agent["y"]))

    def step(self):
        self.schedule.step()
    
    def run_model(self, n):
        for i in range(n):
            self.step()

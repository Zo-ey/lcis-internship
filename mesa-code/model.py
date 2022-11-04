from mesa import Model
from mesa.space import SingleGrid
from mesa.time import RandomActivation
from agent import AgentVanet


class ModelVanet(Model):
    def __init__(self):
        self.running = True
        self.grid = SingleGrid(800, 600, False)
        self.schedule = RandomActivation(self)
        a = AgentVanet(0, self)
        self.schedule.add(a)
        self.grid.place_agent(a, (0, 0))

    def step(self):
        self.schedule.step()


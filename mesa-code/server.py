import mesa
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from model import ModelVanet


def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",
        "color": "grey",
        "Filled": "true",
        "r": 0.5,
        "Layer": 0,
    }
    return portrayal

model_params = {
}

def start(scenario, port, open_browser):
    grid = CanvasGrid(agent_portrayal, 10, 10, 600, 600)
    server = ModularServer(
        ModelVanet, [grid], "VANET Model", model_params
    )

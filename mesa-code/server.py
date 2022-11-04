import mesa
from mesa.visualization.modules.CanvasGridVisualization import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from model import ModelVanet


def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "true", "r": 0.5, "Layer": 1}
    portrayal["Color"] = "grey"
    return portrayal

grid = CanvasGrid(agent_portrayal, 800, 600, 800, 600)
model_params = {
    "width": 800,
    "height": 600,
}

server = ModularServer(
    ModelVanet, [grid], "VANET Model"
)

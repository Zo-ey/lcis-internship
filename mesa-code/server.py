import mesa
#from mesa.visualization.modules.CanvasGridVisualization import CanvasGrid
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

grid = CanvasGrid(agent_portrayal, 10, 10, 600, 600)
model_params = {
}

server = ModularServer(
    ModelVanet, [grid], "VANET Model", model_params
)

#server.launch()


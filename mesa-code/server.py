import mesa

from model import ModelVanet


def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "true", "r": 0.5, "Layer": 1}
    portrayal["Color"] = "grey"
    return portrayal

grid = mesa.visualization.CanvasGrid(agent_portrayal, 800, 600, 800, 600)
model_params = {
    "width": 800,
    "height": 600,
}

server = mesa.visualization.ModularServer(
    ModelVanet, [grid], "VANET Model"
)

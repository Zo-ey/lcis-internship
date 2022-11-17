import mesa
#from mesa.visualization.modules import CanvasGrid
#from mesa.visualization.ModularVisualization import ModularServer

from model import ModelVanet


def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",
        "color": "red",
        "Filled": "true",
        "r": 0.5,
        "Layer": 0,
    }
    return portrayal

def start(scenario, port, open_browser):
    grid = mesa.visualization.CanvasGrid(agent_portrayal, scenario["model"]["width"], scenario["model"]["height"], 500, 500)
    server = mesa.visualization.ModularServer(
        ModelVanet, [grid], "VANET Model", scenario, port
    )
    server.launch(port, open_browser)

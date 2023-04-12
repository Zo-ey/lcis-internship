import os
import yaml
from pathlib import Path

import server
from model import WSNModel
from wsn_message import WSNMessage


DEFAULT_NB_STEPS = 20
#TODO: change file names management for default names + user custom names
PROFILE_FIFO = "./profile-dt-mas-fifo"
MESS_FIFO = "./messages-dt-mas-fifo"
AGENT_DEFAULTS = {
    "color": "black",
}


def get2(dictionary, key, default):
    """ Just like `dict.get()` but also return the default if the `dict[key]` is `None` """
    result = dictionary.get(key, default)
    if result is None:
        result = default
    return result










def load_parameters(profile_file):
    """ Parse the profile file and add default values """
    with open(profile_file, 'r') as f:
        yaml_profile = yaml.safe_load(f)
    # print(yaml_profile)
    profile = {"model": yaml_profile["model"], "agents": {}}
    f.close()

    for class_name, agents in yaml_profile["agents"].items():
        profile["agents"][class_name] = []

        for i, agent in enumerate(agents):
            profile["agents"][class_name].append({
                "id": i,
                "x": agent["x"],
                "y": agent["y"],
                "color": get2(agent, "color", AGENT_DEFAULTS["color"]),
            })
            
    return profile


# If ran by `mesa runserver`
if __name__ == "builtins":
    # load_parameters() does not seem to have access to top level import, functions definitions or
    # global variables if used from here
    import sys
    print("'mesa runserver' is not available, use the 'run.py'", file=sys.stderr)
    exit(1)

# If ran directly with `python run.py`
if __name__ == "__main__":
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(
        description="Run the model",
        formatter_class = ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-p",
        "--profile",
        type = Path,
        default = PROFILE_FIFO,
        help = "the agents configuration in the simulator (currently not working)"#TODO: change when corrected
    )
    parser.add_argument(
        "-t",
        "--threshold",
        type = int,
        default = 5,
        help = "Define threshold percentage for blackhole detection. Default is 5%"
    )
    subparsers = parser.add_subparsers(dest="command")
    gui_parser = subparsers.add_parser(
        "gui",
        help = "Start a HTTP server on port to present the simulation"
    )
    gui_parser.add_argument(
        "-P",
        "--port",
        type = int,
        default = None,
        help = "The port used by the HTTP server (see Mesa for the default value)"
    )
    gui_parser.add_argument(
        "-O",
        "--open_browser",
        type = bool,
        default = True,
        help = "Open a web browser if none is running yet"
    )
    tui_parser = subparsers.add_parser(
        "tui",
        help = "Only run model for a given number of steps then stops (default)",
    )
    tui_parser.add_argument(
        "-s",
        "--steps-count",
        type = int,
        default = DEFAULT_NB_STEPS,
        help = "the number of steps"
    )

    # Parse argument and get Mesa profile from profile file path
    args = parser.parse_args()
    profile = load_parameters(args.profile)

    # Start the GUI
    if args.command == "gui":
        server.start(profile, args.port, args.open_browser)

    # Run the model without the server
    else:
        # Get the step count
        try:
            steps_count = args.steps_count
        except AttributeError:
            steps_count = DEFAULT_NB_STEPS

        # Initialization
        profile["model"].pop("name")
        model = WSNModel(profile["agents"], **profile["model"])
        with open(MESS_FIFO, 'r') as f:
            messages = yaml.safe_load(f)

        # Beginning of the simulation
        print(f"seed: {model.seed}")
        for i in range(steps_count):
            print(f"step:{i}")
            model.step(messages)

import os

fifo_name = "./dt-mas-fifo"
default_ex = b'''
# -1 means broadcast
model:
    name: "Blackhole Profile"
    width: 10
    height: 10
    seed: null
    messages_path: messages.yaml

agents:
  agent.WSNAgent:
    - id: 0
      x: 0
      y: 0
      color: "black"
      seed: null
    - id: 1
      x: 5
      y: 5
      color: "black"
      seed: null
    - id: 2
      x: 1
      y: 5
      color: "black"
      seed: null
    - id: 3
      x: 0
      y: 8
      color: "black"
      seed: null
    - id: 4
      x: 8
      y: 0
      color: "black"
      seed: null
'''
if not os.path.exists(fifo_name):
    try:
        x = os.mkfifo(fifo_name)
    except OSError:
        print("Failed fifo creation")
    else:
        pass

fifo_out = os.open(fifo_name, os.O_WRONLY)
os.write(fifo_out, default_ex)


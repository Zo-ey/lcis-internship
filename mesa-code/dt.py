import os

#TODO: change file names management for default names + user custom names (with parser like run.py)
profile_fifo_name = "./profile-dt-mas-fifo"
messages_fifo_name = "./messages-dt-mas-fifo"
default_ex = b'''
# -1 means broadcast
model:
    name: "Blackhole Profile"
    width: 10
    height: 10
    seed: null

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
messages = b'''
0: # blackhole
  - src: 0
    dest: -1
    message_type: Advertisement
    data: 0x00
1: # suspicious
  - src: 0
    dest: -1
    message_type: Advertisement
    data: 0x00
  - src: 3
    dest: 1
    message_type: Data
    data: 0x00
2:
  - src: 0
    dest: -1
    message_type: Advertisement
    data: 0x00
  - src: 2
    dest: 4
    message_type: Data
    data: 0x00
  - src: 4
    dest: 2
    message_type: Data
    data: 0x01
3:
  - src: 0
    dest: -1
    message_type: Advertisement
    data: 0x00
  - src: 3
    dest: 1
    message_type: Data
    data: 0x00
4:
  - src: 0
    dest: -1
    message_type: Advertisement
    data: 0x00
  - src: 2
    dest: 4
    message_type: Data
    data: 0x00
  - src: 4
    dest: 2
    message_type: Data
    data: 0x01
'''

if not os.path.exists(profile_fifo_name):
    try:
        os.mkfifo(profile_fifo_name)
    except OSError:
        print("Failed profile fifo creation")
    else:
        pass
out_p =  os.open(profile_fifo_name, os.O_WRONLY)
os.write(out_p, default_ex)
os.close(out_p)

if not os.path.exists(messages_fifo_name):
    try:
        os.mkfifo(messages_fifo_name)
    except OSError:
        print("Failed messages fifo creation")
    else:
        pass
out_m = os.open(messages_fifo_name, os.O_WRONLY)
os.write(out_m, messages)


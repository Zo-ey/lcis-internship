import socket
import time
import yaml

# Dictionary to store information about messages sent and received by clients
message_info = {}

# Create a socket and bind it to a port
server_socket = socket.socket()
server_socket.bind(("localhost", 8000))

# Listen for incoming connections
server_socket.listen()

# Continuously accept incoming connections and receive information about messages
while True:
    # Accept an incoming connection
    client_socket, client_address = server_socket.accept()
    print("Received connection from", client_address)
    
    # Receive message information from the client
    data = client_socket.recv(1024)
    
    # Parse the received data
    source, destination, message_type = data.split(" ")
    
    # Store the received information in the message_info dictionary
    message_info[source] = (destination, message_type)
    
    # Every 10 seconds, write the contents of the message_info dictionary to a YAML file
    if time.time() % 10 == 0:
        with open("message_info.yml", "w") as file:
            yaml.dump(message_info, file)

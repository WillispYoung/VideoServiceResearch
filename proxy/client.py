import select
import socket
import json

config = json.load("config.json")


def create_remote():
    remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote.connect((config["server_ip"], config["server_port"]))
    remote.setblocking(0)
    return remote


manager = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
manager.setblocking(0)

manager.bind(('localhost', config['manager_port']))
manager.listen(10)

inputs = [manager]

local2remote = {}
remote2local = {}

while inputs:
    readable, _, _ = select.select(inputs, [], [])

    for s in readable:
        if s is manager:
            client, _ = manager.accept()
            client.setblocking(0)
            inputs.append(client)

            remote = create_remote()
            local2remote[client] = remote
            remote2local[remote] = client
        
        else:
            data = s.recv(4096)
            




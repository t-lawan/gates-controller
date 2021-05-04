import socket
import sys

class Client:
    def __init__(self):
        print("INIT")

    ip = "192.168.0.0.1"
    port = 1234  # web

    def send(self, schedule_action):
        print("")
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))
        self.s.send("TEST")
        self.s.close()


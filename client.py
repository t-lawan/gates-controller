import socket
import sys
import json

class Client:
    def __init__(self):
        print("INIT CLIENT")

    ip = "192.168.0.1"
    port = 1234  # web
    def convert_action_to_json(self, schedule_action):
        x = {
            "command": schedule_action.command,
            "gate_id": schedule_action.gate_id,
            "time": schedule_action.time
        }
        return x

    def set_ip(self, schedule_action):
        if schedule_action.gate_id == "GATE_1":
            self.ip = "192.168.1.1"
        elif schedule_action.gate_id == "GATE_2":
            self.ip = "192.168.1.2"
        elif schedule_action.gate_id == "GATE_3":
            self.ip = "192.168.1.3"
        elif schedule_action.gate_id == "GATE_4":
            self.ip = "192.168.1.4"

    def send(self, schedule_action):
        try:
            self.set_ip(schedule_action)
            jsonString = self.convert_action_to_json(schedule_action)
            print("SCHEDULE_ACTION", jsonString)
            # self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # self.s.connect((self.ip, self.port))
            # self.s.send("TEST")
            # self.s.close()
        except:
            print("Error send data to: ", schedule_action.gate_id)


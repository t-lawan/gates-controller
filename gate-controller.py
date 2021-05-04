import csv
import os
from action import Action
from action import Action
import time
import sys

class GateController:
    index = 0
    interval = 1
    last_time = 0
    last_break_time = 0
    delay_time = 1 * 60
    is_running = False
    action_list = []
    
    def __init__(self):
        print("INIT")
    def start(self):
        print("START")
        self.load_csv()
        while True:
            self.run_schedule()
        
    def load_csv(self):
        print("LOAD CSV")
#        Load CSV File in Directory
        __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
        csvFile = open(os.path.join(__location__, 'sequence.csv'))
        
#        Add CSV file into action_list
        data = csv.reader(csvFile)
        scheduleList = list(data)
        for row in scheduleList:
#        COMMAND, GATE_ID, TIME
            act = Action(row[2], row[1], int(row[0]) + 1)
            self.action_list.append(act)
            
        max_time = self.find_max_time()
        schedule_action = Action("STOP", "0", max_time + 1)
        self.action_list.append(schedule_action)
            
    
    def find_max_time(self):
        maxValue = 1
        for schedule_action in self.action_list:
            if schedule_action.time >= maxValue:
                maxValue = schedule_action.time
        return maxValue
        
        
    def run_task(self, schedule_action, current_time):
        print(schedule_action.time, schedule_action.command)
        if schedule_action.command == "STOP":
            print("STOP TASK")
            self.break_time = current_time
            sys.exit()
            # Take a break
        else:
            print("RUNNING TASK")
        
        
    def run_schedule(self):
#        Count Every Second
        current_time = time.perf_counter()
        if(current_time - self.last_time  >= self.interval):
            actions_to_call = self.find_all_actions(current_time)
            if(len(actions_to_call) > 0):
                for schedule_action in actions_to_call:
                    self.run_task(schedule_action, current_time)
            self.last_time = current_time
        
    def find_all_actions(self, second):
        filtered_list = list(filter(lambda act: act.time == int(second), self.action_list))
        return filtered_list
        

gateController = GateController()
gateController.start()

        
            
            

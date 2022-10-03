from random import randint
from process import Process
from program import Program
from pcb import PCB
from time_tracker import TimeTracker


class Scheduler:

    def __init__(self, time_tracker: TimeTracker):
        self.time = 0
        self.step = 1

        self.processes = []
        
        self.new = []    
        self.processes = []
        self.ready = []

        self.running = None
        self.until = 0

        self.blocked = []
        self.exit = []

        self.time_tracker = time_tracker

    
    def add_process(self, path, arrival, quantum, priority=2):
        program = Program(path)
        process = Process(program)
        pcb = PCB(process, arrival, quantum, priority)

        self.new.append(pcb)


    def run(self):
        while self.ready or self.blocked or self.new or self.running:
            self.handle_new()
            
            if self.running:
                result = self.running.process.step()
                self.handle_result(result)

            if self.time >= self.until:
                self.schedule()

            self.time += self.step


    def schedule(self):
        self.handle_blocked()        

        if self.running:
            self.time_tracker.register_event(self.time, self.running.pid, 'ready')
            self.ready.append(self.running) # w/o priority
        
        if self.ready:
            self.running = self.ready.pop(0)
            self.until = self.time + self.running.timeout
            self.time_tracker.register_event(self.time, self.running.pid, 'running')
    
    
    def handle_new(self):
        for pcb in self.new:
            if  pcb.arrival <= self.time:
                self.new.remove(pcb)
                self.ready.append(pcb)
                self.time_tracker.register_event(self.time, pcb.pid, 'ready')
    

    def handle_result(self, result):
        if result == None:
            return
        
        if result == Process.EXIT:
            self.time_tracker.register_event(self.time, self.running.pid, 'exited')
            self.exit.append(self.running)
            self.running = None
        
        if result in [Process.PRINT, Process.INPUT]:
            self.time_tracker.register_event(self.time, self.running.pid, 'blocked')
            self.blocked.append((self.running, self.time + randint(10, 15)))
            self.running = None

        # self.schedule()

    
    def handle_blocked(self):
        for blocked in self.blocked:
            pcb, time = blocked

            if self.time >= time:
                self.blocked.remove(blocked)
                self.ready.append(pcb)
                self.time_tracker.register_event(self.time, pcb.pid, 'ready')
         

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣷⣶⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡟⠁⣰⣿⣿⣿⡿⠿⠻⠿⣿⣿⣿⣿⣧⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠏⠀⣴⣿⣿⣿⠉⠀⠀⠀⠀⠀⠈⢻⣿⣿⣇⠀⠀⠀
# ⠀⠀⠀⠀⢀⣠⣼⣿⣿⡏⠀⢠⣿⣿⣿⠇kinda sus⠈⣿⣿⣿⠀⠀
# ⠀⠀⠀⣰⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀⠀hessel⠀ ⣿⣿⣿⡇⠀⠀
# ⠀⠀⢰⣿⣿⡿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣿⠀⠀
# ⠀⠀⣿⣿⣿⠁⣿⣿⣿⡇⠀⠀⠻⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⠃⠀⠀⠀
# ⠀⢰⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
# ⠀⢸⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠉⢉⣿⣿⠀⠀⠀⠀⠀⠀
# ⠀⢸⣿⣿⣇⠀⣿⣿⣿⠀⠀⠀⠀⠀⢀⣤⣤⣤⡀⠀⠀⢸⣿⣿⣿⣷⣦⠀⠀⠀
# ⠀⠀⢻⣿⣿⣶⣿⣿⣿⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⡀⠀⠉⠉⠻⣿⣿⡇⠀⠀
# ⠀⠀⠀⠛⠿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠈⠹⣿⣿⣇⣀⠀⣠⣾⣿⣿⡇⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣦⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠛⠋⠉⠉⠁⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁
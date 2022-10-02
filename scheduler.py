from random import randint
from process import Process
from program import Program
from pcb import PCB


class Scheduler:

    def __init__(self):
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

    
    def add_process(self, path, arrival, quantum, priority=2):
        program = Program(path)
        process = Process(program)
        pcb = PCB(process, arrival, quantum, priority)

        self.new.append(pcb)


    def run(self):
        while self.ready or self.blocked or self.new or self.running:
            if self.time >= self.until:
                self.schedule()
            
            if self.running:
                result = self.running.process.step()
                self.handle_result(result)

            self.time += self.step
        
        print(f'time: {self.time}, simulation ended')


    def schedule(self):
        self.handle_blocked()
        self.handle_new()

        if self.running:
            print(f'time: {self.time}, to ready: {self.running.pid}')
            self.ready.append(self.running) # w/o priority
        
        if self.ready:
            self.running = self.ready.pop(0)
            self.until = self.time + self.running.quantum
            print(f'time: {self.time}, to running: {self.running.pid}')
    
    
    def handle_new(self):
        for pcb in self.new:
            if  pcb.arrival == self.time:
                self.new.remove(pcb)
                self.ready.append(pcb)
                print(f'time: {self.time}, process arrived: {pcb.pid}')
    

    def handle_result(self, result):
        if result == None:
            return
        
        if result == Process.EXIT:
            print(f'time: {self.time}, process exited: {self.running.pid}')
            self.exit.append(self.running)
            self.running = None
        
        if result in [Process.PRINT, Process.INPUT]:
            print(f'time: {self.time}, process blocked: {self.running.pid} ({result})')
            self.blocked.append((self.running, self.time + randint(10, 15)))
            self.running = None

        self.schedule()

    
    def handle_blocked(self):
        for blocked in self.blocked:
            pcb, time = blocked

            if self.time >= time:
                self.blocked.remove(blocked)
                self.ready.append(pcb)
                print(f'time: {self.time}, process unblocked: {pcb.pid}')
         

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